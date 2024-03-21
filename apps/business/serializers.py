from email.policy import default
from rest_framework import serializers
from django.contrib.auth import get_user_model


# from apps.tour.serializers import TourListSerializer
from .models import (
    TourAgent,
    TourAgentImage
)


from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TourAgent

User = get_user_model()


class TourAgentCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TourAgent
        fields = '__all__'

    def create(self, validated_data):
        profile = TourAgent.objects.create(**validated_data)
        # Устанавливаем is_business пользователя на True после создания профиля
        user = profile.user
        user.is_business = True
        user.save()
        return profile
     

class TourAgentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourAgentImage
        fields = 'image',


class TourAgentSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TourAgent
        fields = '__all__'

    # def to_representation(self, instance):         
    #     rep =  super().to_representation(instance)
    #     rep['tour'] = TourListSerializer(
    #         instance.title.all(), many=True
    #     ).data
    #     return rep


class TourAgentListSerializer(serializers.ModelSerializer):

     class Meta:
        model = TourAgent
        fields = ['title', 'phone', 'email', 'address']


class TourAgentUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TourAgent
        fields = '__all__'
