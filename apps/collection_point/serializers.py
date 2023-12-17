from rest_framework import serializers

from apps.collection_point.models import CollectionPoint
from apps.tags.models import TouristRegion
from apps.tags.serializers import TouristRegionSerializer


class CollectionPointSerializer(serializers.ModelSerializer):
    tourist_region = TouristRegionSerializer(many=True)

    class Meta:
        model = CollectionPoint
        fields = ('address', 'description', 'tourist_region')

    def create(self, validated_data):
        tourist_region_data = validated_data.pop('tourist_region')
        collection_point = CollectionPoint.objects.create(**validated_data)

        for tourist_regions_data in tourist_region_data:
            TouristRegion.objects.create(collection_point=collection_point, **tourist_regions_data)

        return collection_point
