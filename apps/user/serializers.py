from rest_framework import serializers, status
from django.contrib.auth import get_user_model

from .models import Profile, ProfileImage
from .utils import normalize_phone

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )
    carousel_img = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        carousel_images = validated_data.pop('carousel_img')
        profile = Profile.objects.create(**validated_data)
        images = []

        for image in carousel_images:
            images.append(ProfileImage(user=profile, image=image))

        ProfileImage.objects.bulk_create(images)
        return profile

    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user
        return attrs

    # def validate(self, attrs):
    #     user = self.context['request'].user
    #     attrs['user'] = user
    #     return attrs
    
    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неправильный формат номера телефона.')
        return phone


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        fields = '__all__'
        model = Profile


    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user
        return attrs
    

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = 'image',