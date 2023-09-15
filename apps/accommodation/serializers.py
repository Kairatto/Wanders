from rest_framework import serializers
from .models import HotelImages, Hotel, Accommodation


class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = ('image',)


class HotelSerializer(serializers.ModelSerializer):
    hotel_images = HotelImagesSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('slug', 'title_hotel', 'description_hotel', 'hotel_images')

    def create(self, validated_data):
        hotel_images_data = validated_data.pop('hotel_images', [])
        hotels = Hotel.objects.create(**validated_data)

        for hotels_images_data in hotel_images_data:
            HotelImages.objects.create(hotels=hotels, **hotels_images_data)

        return hotels


class AccommodationSerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True)

    class Meta:
        model = Accommodation
        fields = ('slug', 'title_accommodation', 'description_accommodation', 'comfort', 'type', 'hotels')

    def create(self, validated_data):
        hotel_data = validated_data.pop('hotels')
        accommodations = Accommodation.objects.create(**validated_data)

        for hotels_data in hotel_data:
            Hotel.objects.create(accommodations=accommodations, **hotels_data)

        return accommodations
