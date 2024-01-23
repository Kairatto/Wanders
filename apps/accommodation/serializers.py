from rest_framework import serializers
from .models import Place, PlaceResidence, PlaceResidenceImages


class PlaceResidenceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceResidenceImages
        fields = ('image',)

#
# class AccommodationImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccommodationImages
#         fields = ('image',)


class PlaceResidenceSerializer(serializers.ModelSerializer):
    place_residence_images = PlaceResidenceImagesSerializer(many=True)

    class Meta:
        model = PlaceResidence
        fields = ('title', 'description', 'type_accommodation', 'place_residence_images')

    def create(self, validated_data):
        place_residence_images_data = validated_data.pop('place_residence_images')
        place_residence = PlaceResidence.objects.create(**validated_data)

        for place_residence_image_data in place_residence_images_data:
            PlaceResidenceImages.objects.create(place_residence=place_residence, **place_residence_image_data)

        return place_residence


class PlaceSerializer(serializers.ModelSerializer):
    place_residence = PlaceResidenceSerializer(many=True)

    class Meta:
        model = Place
        fields = ('amount_days', 'place_residence')

    def create(self, validated_data):
        place_residence_data = validated_data.pop('place_residence_data')
        place = Place.objects.create(**validated_data)

        for places_residence_data in place_residence_data:
            PlaceResidenceImages.objects.create(place=place, **places_residence_data)

        return place

#
# class AccommodationSerializer(serializers.ModelSerializer):
#
#     accommodation_images = AccommodationImagesSerializer(many=True)
#
#     class Meta:
#         model = Accommodation
#         fields = ('description', 'accommodation_images')
#
#     def create(self, validated_data):
#         accommodation_image_data = validated_data.pop('accommodation_images')
#         accommodations = Accommodation.objects.create(**validated_data)
#
#         for accommodation_images_data in accommodation_image_data:
#             AccommodationImages.objects.create(accommodation=accommodations, **accommodation_images_data)
#
#         return accommodations
