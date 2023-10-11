from rest_framework import serializers
from .models import TourDescription, DescriptionDetail


class DescriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionDetail
        fields = ('image', 'title_detail', 'description_detail')


class TourDescriptionSerializer(serializers.ModelSerializer):
    description_details = DescriptionDetailSerializer(many=True)

    class Meta:
        model = TourDescription
        fields = ('description', 'description_details')

    def create(self, validated_data):
        description_detail_data = validated_data.pop('description_details')
        tour_description = TourDescription.objects.create(**validated_data)

        for description_details_data in description_detail_data:
            DescriptionDetail.objects.create(tour_description=tour_description, **description_details_data)

        return tour_description
