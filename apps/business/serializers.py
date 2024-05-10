from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg

from .models import TourAgent
from ..review.models import Review
from ..tour.models import Tour
from ..tour.serializers import SimilarTourSerializer

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
    average_rating = serializers.SerializerMethodField()
    organizer_tours = serializers.SerializerMethodField()
    total_reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = TourAgent
        fields = ['slug', 'title', 'desc', 'image', 'additional_contacts', 'phone', 'email', 'instagram', 'is_verified',
                  'average_rating', 'total_reviews_count', 'organizer_tours']

    def get_total_reviews_count(self, obj):
        user = obj.user
        total_reviews = Review.objects.filter(tour__author=user).count()
        return total_reviews

    def get_average_rating(self, obj):
        # Получаем пользователя, связанного с TourAgent
        user = obj.user
        # Рассчитываем средний рейтинг для всех туров, связанных с этим пользователем
        average_rating = Review.objects.filter(tour__author=user).aggregate(Avg('rating'))['rating__avg']
        return round(average_rating, 1) if average_rating is not None else None

    def get_organizer_tours(self, obj):
        user = obj.user
        tours = Tour.objects.filter(author=user)  # Получаем все туры, связанные с пользователем
        return SimilarTourSerializer(tours, many=True, context=self.context).data


class TourAgentListSerializer(serializers.ModelSerializer):

     class Meta:
        model = TourAgent
        fields = ['slug', 'title', 'phone', 'email', 'instagram', 'is_verified']


class TourAgentUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.email',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TourAgent
        fields = '__all__'
