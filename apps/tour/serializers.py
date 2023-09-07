from rest_framework import serializers
from .models import Days, DaysImage


class DaysCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Days
        fields = '__all__'

    day_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        day_carousel = validated_data.pop('day_image_carousel')
        day = Days.objects.create(**validated_data)
        images = []
        for image in day_carousel:
            images.append(DaysImage(day=day, image=image))
        DaysImage.objects.bulk_create(images)
        day.save()

        return day


class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = DaysImageSerializer(
            instance.days_images.all(), many=True
        ).data
        return representation


class DaysListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = '__all__'


class DaysImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysImage
        fields = 'image',
