from rest_framework import serializers
from .models import Place, PlaceResidence, PlaceResidenceImages


class PlaceResidenceImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceResidenceImages
        fields = ('image',)


class PlaceResidenceSerializer(serializers.ModelSerializer):
    place_residence_images = PlaceResidenceImagesSerializer(many=True, required=False)

    class Meta:
        model = PlaceResidence
        fields = ('title', 'description', 'type_accommodation', 'place_residence_images')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        choice_fields = {'type_accommodation': dict(PlaceResidence.TYPE_ACCOMMODATION_CHOICES)}
        for field, choices in choice_fields.items():
            value = representation.get(field)
            if value is not None:
                representation[field] = choices.get(value)

        return representation

    def create(self, validated_data):
        place_residence_images_data = validated_data.pop('place_residence_images')
        place_residence = PlaceResidence.objects.create(**validated_data)

        for place_residence_image_data in place_residence_images_data:
            PlaceResidenceImages.objects.create(place_residence=place_residence, **place_residence_image_data)

        return place_residence


class PlaceSerializer(serializers.ModelSerializer):
    place_residence = PlaceResidenceSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = ('amount_days', 'place_residence')

    def create(self, validated_data):
        place_residence_data = validated_data.pop('place_residence_data')
        place = Place.objects.create(**validated_data)

        for places_residence_data in place_residence_data:
            PlaceResidenceImages.objects.create(place=place, **places_residence_data)

        return place
