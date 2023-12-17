from rest_framework import serializers
from .models import PlaceImages, Place, Accommodation, AccommodationImages, AnotherPlaceImages, AnotherPlace


class PlaceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImages
        fields = ('image',)


class AnotherPlaceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnotherPlaceImages
        fields = ('image',)


class AccommodationImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationImages
        fields = ('image',)


class AnotherPlaceSerializer(serializers.ModelSerializer):
    another_place_images = AnotherPlaceImagesSerializer(many=True)

    class Meta:
        model = AnotherPlace
        fields = ('title', 'description', 'amount_days', 'type_accommodation', 'another_place_images')

    def create(self, validated_data):
        another_place_images_data = validated_data.pop('another_place_images')
        another_place = AnotherPlace.objects.create(**validated_data)

        for another_places_images_data in another_place_images_data:
            AnotherPlaceImages.objects.create(another_place=another_place, **another_places_images_data)

        return another_place


class PlaceSerializer(serializers.ModelSerializer):
    place_images = PlaceImagesSerializer(many=True)
    another_place = AnotherPlaceSerializer(many=True)

    class Meta:
        model = Place
        fields = ('title', 'description', 'amount_days', 'type_accommodation', 'place_images', 'another_place')

    def create(self, validated_data):
        place_images_data = validated_data.pop('place_images')
        place = Place.objects.create(**validated_data)

        for places_images_data in place_images_data:
            PlaceImages.objects.create(place=place, **places_images_data)

        return place


class AccommodationSerializer(serializers.ModelSerializer):

    accommodation_images = AccommodationImagesSerializer(many=True)

    class Meta:
        model = Accommodation
        fields = ('description', 'accommodation_images')

    def create(self, validated_data):
        accommodation_image_data = validated_data.pop('accommodation_images')
        accommodations = Accommodation.objects.create(**validated_data)

        for accommodation_images_data in accommodation_image_data:
            AccommodationImages.objects.create(accommodation=accommodations, **accommodation_images_data)

        return accommodations
