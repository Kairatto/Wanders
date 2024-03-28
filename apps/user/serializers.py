from rest_framework import serializers, status
from django.contrib.auth import get_user_model

from .models import Profile, ProfileImage
from .utils import normalize_phone

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.email'
    )
    user_image = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        if Profile.objects.filter(user=user).exists():
            raise serializers.ValidationError("У вас уже есть созданный аккаунт")

        validated_data['user'].is_user = True
        validated_data['user'].save()

        user_images = validated_data.pop('user_image')
        profile = Profile.objects.create(**validated_data)
        images = []

        for image in user_images:
            images.append(ProfileImage(user=profile, image=image))

        ProfileImage.objects.bulk_create(images)
        return profile

    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user
        return attrs

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неправильный формат номера телефона.')
        return phone


class ProfileListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'phone', 'country', 'city']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.email'
    )

    class Meta:
        model = Profile
        fields = '__all__'

    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user
        return attrs
    

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = 'image',
