from rest_framework import serializers

from apps.tags.models import City, Country, Collection, Location, Activity, TouristRegion


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('activity',)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city', )


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('country', )


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('collection', )


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('location', )


class TouristRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TouristRegion
        fields = ('region', )
