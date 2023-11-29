from rest_framework import serializers

from .models import TourDescription, DescriptionDetail


class DescriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionDetail
        fields = ('image', 'title', 'description')


class TourDescriptionSerializer(serializers.ModelSerializer):
    description_details = DescriptionDetailSerializer(many=True, required=False)

    class Meta:
        model = TourDescription
        fields = ('description', 'description_details')

    def create(self, validated_data):
        description_details_data = validated_data.pop('description_details', None)
        tour_description = TourDescription.objects.create(**validated_data)

        if description_details_data is not None:
            for description_detail_data in description_details_data:
                DescriptionDetail.objects.create(tour_description=tour_description, **description_detail_data)

        return tour_description
