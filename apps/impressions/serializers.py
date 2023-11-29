from rest_framework import serializers
from .models import Tour, Impression, ImpressionImages


class ImpressionImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpressionImages
        fields = ('image',)


class ImpressionSerializer(serializers.ModelSerializer):
    impression_images = ImpressionImagesSerializer(many=True)

    class Meta:
        model = Impression
        fields = ('slug', 'title', 'description', 'impression_images')

    def create(self, validated_data):
        impression_images_data = validated_data.pop('impression_images')
        impressions = Impression.objects.create(**validated_data)

        for impression_image_data in impression_images_data:
            ImpressionImages.objects.create(impression=impressions, **impression_image_data)

        return impressions
