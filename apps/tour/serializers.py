from rest_framework import serializers
from .models import Tour
from apps.days.models import Days, DaysImage
from apps.days.serializers import DaysSerializer
from apps.accommodation.serializers import AccommodationSerializer
from apps.accommodation.models import Accommodation, Hotel, HotelImages
from apps.tour_images.serializers import TourImagesSerializer
from apps.important_information.serializers import ImportantInformationSerializer
from apps.important_information.models import ImportantInformation
from apps.tour_images.models import TourImages


class TourSerializer(serializers.ModelSerializer):
    tour_images = TourImagesSerializer(many=True)
    days = DaysSerializer(many=True)
    accommodations = AccommodationSerializer(many=True)
    important_informations = ImportantInformationSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('slug', 'title_tour', 'text_tour', 'tour_images', 'days', 'accommodations', 'important_informations', 'create_date')

    def create(self, validated_data):
        tour_images_data = validated_data.pop('tour_images')
        days_data = validated_data.pop('days')
        accommodation_data = validated_data.pop('accommodations')
        important_informations_data = validated_data.pop('important_informations')
        tour = Tour.objects.create(**validated_data)

        for day_data in days_data:
            days_images_data = day_data.pop('days_images', [])
            days = Days.objects.create(tour=tour, **day_data)
            for image_data in days_images_data:
                DaysImage.objects.create(day=days, **image_data)

        for tour_image_data in tour_images_data:
            tour_image_data.pop('tour_images', [])
            TourImages.objects.create(tour=tour, **tour_image_data)

        for important_information_data in important_informations_data:
            important_information_data.pop('important_informations', [])
            ImportantInformation.objects.create(tour=tour, **important_information_data)

        for accommodations_data in accommodation_data:
            hotel_data = accommodations_data.pop('hotels', [])
            accommodations = Accommodation.objects.create(tour=tour, **accommodations_data)
            for hotels_data in hotel_data:
                hotels_images_data = hotels_data.pop('hotel_images', [])
                hotels = Hotel.objects.create(accommodation=accommodations, **hotels_data)
                for hotel_image_data in hotels_images_data:
                    HotelImages.objects.create(hotel=hotels, **hotel_image_data)

        return tour
