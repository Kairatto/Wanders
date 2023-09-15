from rest_framework import serializers
from .models import Tour, Days, DaysImage


class DaysImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysImage
        fields = ('image',)


class DaysSerializer(serializers.ModelSerializer):
    days_images = DaysImageSerializer(many=True)

    class Meta:
        model = Days
        fields = ('slug', 'title_days', 'description_days', 'days_images')

    def create(self, validated_data):
        days_images_data = validated_data.pop('days_images')
        days = Days.objects.create(**validated_data)

        for image_data in days_images_data:
            DaysImage.objects.create(day=days, **image_data)

        return days
