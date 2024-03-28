from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TourAgent

User = get_user_model()


class TourAgentCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.email',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TourAgent
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        if TourAgent.objects.filter(user=user).exists():
            raise serializers.ValidationError('У вас уже есть созданный аккаунт')
        profile = TourAgent.objects.create(user=user, **validated_data)
        user.is_business = True
        user.save()
        return profile


class TourAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourAgent
        fields = '__all__'


class TourAgentListSerializer(serializers.ModelSerializer):

     class Meta:
        model = TourAgent
        fields = ['slug', 'title', 'phone', 'email', 'instagram']


class TourAgentUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.email',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TourAgent
        fields = '__all__'
