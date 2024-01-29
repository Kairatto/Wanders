from rest_framework import serializers

from apps.location_info.models import LocationInfo, LocationInfoImage, GettingThere
from apps.tags.models import Collection, Country, Activity, Location, TouristRegion, MainLocation

from apps.tags.serializers import (CollectionBunchSerializer, CountryBunchSerializer, LocationBunchSerializer,
                                   TouristRegionBunchSerializer, ActivityBunchSerializer, MainLocationBunchSerializer)


class LocationInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfoImage
        fields = ('image',)


class GettingThereSerializer(serializers.ModelSerializer):
    class Meta:
        model = GettingThere
        fields = ('title', 'travel_time', 'price_travel', 'description',)


class LocationInfoSerializer(serializers.ModelSerializer):
    location_info_images = LocationInfoImageSerializer(many=True, required=False)
    getting_there = GettingThereSerializer(many=True, required=False)

    main_location = MainLocationBunchSerializer(many=True, required=False)
    country = CountryBunchSerializer(many=True, required=False)
    activity = ActivityBunchSerializer(many=True, required=False)
    location = LocationBunchSerializer(many=True, required=False)
    collection = CollectionBunchSerializer(many=True, required=False)
    tourist_region = TouristRegionBunchSerializer(many=True, required=False)

    class Meta:
        model = LocationInfo
        fields = ('slug', 'title', 'short_description', 'description', 'how_to_get_there', 'coordinates',
                  'coordinates_map', 'location_info_images', 'getting_there',
                  'main_location', 'activity', 'country', 'collection', 'location', 'tourist_region',)

    def create(self, validated_data):
        location_info_images_data = validated_data.pop('location_info_images', [])
        getting_there_data = validated_data.pop('getting_there', [])

        main_location_data = validated_data.pop('main_location', [])
        countries_data = validated_data.pop('country', [])
        locations_data = validated_data.pop('location', [])
        activities_data = validated_data.pop('activity', [])
        collections_data = validated_data.pop('collection', [])
        tourist_regions_data = validated_data.pop('tourist_region', [])

        location_info = LocationInfo.objects.create(**validated_data)

        location_info.main_location.set([MainLocation.objects.get_or_create(**data)[0] for data in main_location_data])
        location_info.activity.set([Activity.objects.get_or_create(**data)[0] for data in activities_data])
        location_info.collection.set([Collection.objects.get_or_create(**data)[0] for data in collections_data])
        location_info.country.set([Country.objects.get_or_create(**data)[0] for data in countries_data])
        location_info.location.set([Location.objects.get_or_create(**data)[0] for data in locations_data])
        location_info.tourist_region.set([TouristRegion.objects.get_or_create(**data)[0] for data in tourist_regions_data])

        for main_locations_data in main_location_data:
            main_location, created = MainLocation.objects.get_or_create(**main_locations_data)
            location_info.main_location.add(main_location)

        for activity_data in activities_data:
            activity, created = Activity.objects.get_or_create(**activity_data)
            location_info.activity.add(activity)

        for collection_data in collections_data:
            collection, created = Collection.objects.get_or_create(**collection_data)
            location_info.collection.add(collection)

        for country_data in countries_data:
            country, created = Country.objects.get_or_create(**country_data)
            location_info.country.add(country)

        for location_data in locations_data:
            location, created = Location.objects.get_or_create(**location_data)
            location_info.location.add(location)

        for tourist_region_data in tourist_regions_data:
            tourist_region, created = TouristRegion.objects.get_or_create(**tourist_region_data)
            location_info.tourist_region.add(tourist_region)

        for location_info_image_data in location_info_images_data:
            LocationInfoImage.objects.create(location_info=location_info, **location_info_image_data)

        for getting_theres_data in getting_there_data:
            GettingThere.objects.create(location_info=location_info, **getting_theres_data)

        return location_info
