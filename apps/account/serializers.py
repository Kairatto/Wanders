from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

from .tasks import send_activation_code, send_change_password_code


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'The username is taken. choose another one.'
                )
        if not username.replace('_', '').replace('.', '').isalnum(): 
            raise serializers.ValidationError('Username can only contain letters, numbers, an \'_\' and \'.\'')
        if '_.' in username or '._' in username:
            raise serializers.ValidationError('\'_\' and \'.\' cannot stand next to each other')
        if not username[0].isalpha():
            raise serializers.ValidationError('Username must start with a letter')
        return username

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают.')
        return attrs

    def create(self, validated_data): 
        user = User.objects.create_user(**validated_data)
        user.create_activation_code()
        send_activation_code.delay(user.email, user.activation_code)
        return user 


# class ActivationSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50, required=True)
#     code = serializers.CharField(max_length=10, required=True)

#     def validate_user(self, username):
#         if not User.objects.filter(username=username).exists():
#             raise serializers.ValidationError('Пользователя с таким ником не существует.')
#         return username

#     def validate_code(self, code):
#         if not User.objects.filter(activation_code=code).exists():
#             raise serializers.ValidationError('Некорректный код.')
#         return code

#     def activate_account(self):
#         username = self.validated_data.get('username')
#         user = User.objects.get(username=username)
#         user.is_active = True
#         user.activation_code = ''
#         user.save()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_business', 'is_staff', 'is_active', 'activation_code', 'created_at']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=150, required=True)
    new_password = serializers.CharField(max_length=150, required=True)
    new_password_confirm = serializers.CharField(max_length=150, required=True)

    def validate_old_password(self, old_password):
        user = self.context.get('request').user
        if not user.check_password(old_password):
            raise serializers.ValidationError('Неправильнвй пароль!'.upper())
        return old_password

    def validate(self, attrs: dict):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают.'
            )
        if old_password == new_password:
            raise serializers.ValidationError(
                'Старый и новый пароль совпадают.Придумайте новый пароль!!!'
            )
        return attrs

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()


class RestorePasswordSerializer(serializers.Serializer):
    def send_code(self):
        user = self.context.get('request').user
        # print(user)
        # user_email = 
        user = User.objects.get(username=user)
        # print(user)
        user.create_activation_code()
        print(user.email, user.activation_code)
        send_change_password_code.delay(user.email, user.activation_code)


class SetRestoredPasswordSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=1, max_length=10, required=True)
    new_password = serializers.CharField(max_length=128, required=True)
    new_password_confirm = serializers.CharField(max_length=128, required=True)

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError(
                'Некорректный код.'
            )
        return code 

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают.'
            )
        return attrs

    def set_new_password(self): 
        # email = self.validated_data.get('email')
        # user = User.objects.get(email=email)
        user = self.context.get('request').user
        user = User.objects.get(username=user)
        new_password = self.validated_data.get('new_password')
        user.set_password(new_password)
        user.activation_code = ''
        user.save()
