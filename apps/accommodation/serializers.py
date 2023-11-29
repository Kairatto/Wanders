from rest_framework import serializers
from .models import HotelImages, Hotel, Accommodation, AccommodationImages, AnotherHotelImages, AnotherHotel


class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = ('image',)


class AnotherHotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnotherHotelImages
        fields = ('image',)


class AccommodationImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationImages
        fields = ('image',)


class AnotherHotelSerializer(serializers.ModelSerializer):
    another_hotel_images = AnotherHotelImagesSerializer(many=True)

    class Meta:
        model = AnotherHotel
        fields = ('slug', 'title', 'description', 'amount_days', 'another_hotel_images')

    def create(self, validated_data):
        another_hotel_images_data = validated_data.pop('another_hotel_images')
        another_hotels = AnotherHotel.objects.create(**validated_data)

        for another_hotels_images_data in another_hotel_images_data:
            AnotherHotelImages.objects.create(another_hotels=another_hotels, **another_hotels_images_data)

        return another_hotels


class HotelSerializer(serializers.ModelSerializer):
    hotel_images = HotelImagesSerializer(many=True)
    another_hotels = AnotherHotelSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ('slug', 'title', 'description', 'amount_days', 'hotel_images', 'another_hotels')

    def create(self, validated_data):
        hotel_images_data = validated_data.pop('hotel_images')
        hotels = Hotel.objects.create(**validated_data)

        for hotels_images_data in hotel_images_data:
            HotelImages.objects.create(hotels=hotels, **hotels_images_data)

        return hotels


class AccommodationSerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True)
    accommodation_images = AccommodationImagesSerializer(many=True)

    class Meta:
        model = Accommodation
        fields = ('description', 'accommodation_images', 'hotels')

    def create(self, validated_data):
        hotel_data = validated_data.pop('hotels')
        accommodation_image_data = validated_data.pop('accommodation_images')
        accommodations = Accommodation.objects.create(**validated_data)

        for accommodation_images_data in accommodation_image_data:
            Hotel.objects.create(accommodation=accommodations, **accommodation_images_data)

        for hotels_data in hotel_data:
            Hotel.objects.create(accommodation=accommodations, **hotels_data)

        return accommodations
