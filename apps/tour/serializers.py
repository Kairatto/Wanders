from rest_framework import serializers
from .models import Tour
from apps.days.models import Days, DaysImage
from apps.days.serializers import DaysSerializer
from apps.accommodation.serializers import AccommodationSerializer
from ..accommodation.models import Accommodation, Hotel, HotelImages


class TourSerializer(serializers.ModelSerializer):
    days = DaysSerializer(many=True)
    accommodations = AccommodationSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('slug', 'title_tour', 'text_tour', 'days', 'accommodations', 'create_date')

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        accommodation_data = validated_data.pop('accommodations')
        tour = Tour.objects.create(**validated_data)

        for day_data in days_data:
            days_images_data = day_data.pop('days_images', [])
            days = Days.objects.create(tour=tour, **day_data)

            for image_data in days_images_data:
                DaysImage.objects.create(tour=days, **image_data)

        for accommodations_data in accommodation_data:
            hotel_data = accommodations_data.pop('hotels', [])
            accommodations = Accommodation.objects.create(tour=tour, **accommodations_data)

            for hotels_data in hotel_data:
                hotels_images_data = hotels_data.pop('hotel_images')
                hotels = Hotel.objects.create(accommodation=accommodations, **hotels_data)
                for hotel_image_data in hotels_images_data:
                    HotelImages.objects.create(hotels=hotels, **hotel_image_data)

                return tour

        return tour
