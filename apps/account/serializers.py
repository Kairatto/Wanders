from rest_framework import serializers
from django.contrib.auth import get_user_model

from .tasks import send_activation_code, send_change_password_code


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Этот адрес электронной почты уже используется.")
        temporary_email_domains = ['tempmail.com', '10minutemail.com']
        email_domain = value.split('@')[-1]
        if email_domain in temporary_email_domains:
            raise serializers.ValidationError("Пожалуйста, используйте постоянный адрес электронной почты.")

        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'],
                                        password=validated_data['password'])
        user.create_activation_code()
        send_activation_code.delay(user.email, user.activation_code)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_business', 'is_user', 'is_staff', 'is_active', 'activation_code', 'created_at']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=150, required=True)
    new_password = serializers.CharField(max_length=150, required=True)
    new_password_confirm = serializers.CharField(max_length=150, required=True)

    def validate_old_password(self, old_password):
        user = self.context.get('request').user
        if not user.check_password(old_password):
            raise serializers.ValidationError('Неправильный пароль!'.upper())
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
                'Старый и новый пароль совпадают.Придумайте новый пароль!'
            )
        return attrs

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()


class RestorePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def send_code(self):
        email = self.context.get('request').data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            user.create_activation_code()
            send_change_password_code.delay(user.email, user.activation_code)
        else:
            raise serializers.ValidationError('Пользователь с таким email не найден.')


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
        code = self.validated_data.get('code')
        user = User.objects.get(activation_code=code)
        new_password = self.validated_data.get('new_password')
        user.set_password(new_password)
        user.activation_code = ''
        user.save()
