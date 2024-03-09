from email.policy import default
from rest_framework import serializers
from django.contrib.auth import get_user_model


# from apps.tour.serializers import TourListSerializer
from .models import (
    TourAgent,
    TourAgentImage
)


User = get_user_model()


class TourAgentCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TourAgent
        fields = '__all__'

    # def validate_phone(self, phone):
    #     phone = normalize_phone(phone)
    #     if len(phone) != 13:
    #         raise serializers.ValidationError('Invalid phone format!')
    #     return phone  

    def create(self, validated_data):
        profile = TourAgent.objects.create(**validated_data)
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
