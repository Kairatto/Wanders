from rest_framework import serializers
from apps.tour.utils import get_author_info

from apps.tour.models import Tour
from apps.account.serializers import UserSerializer
from apps.tags.models import Collection, Country, Location, TouristRegion
from apps.location_info.models import LocationInfo, LocationInfoImage, GettingThere

from apps.tags.serializers import (CollectionBunchSerializer, CountryBunchSerializer, LocationBunchSerializer,
                                   TouristRegionBunchSerializer)
from apps.concrete_tour.serializers import ConcreteTourDateSerializer
from apps.tour_images.serializers import TourImagesSerializer


class LocationInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfoImage
        fields = ('image',)


class GettingThereSerializer(serializers.ModelSerializer):
    class Meta:
        model = GettingThere
        fields = ('title', 'travel_time', 'price_travel', 'description',)


class TourForLocationSerializer(serializers.ModelSerializer):
    tour_images = TourImagesSerializer(many=True, required=False)
    country = CountryBunchSerializer(many=True, required=False)
    concrete_tour_date = ConcreteTourDateSerializer(many=True, required=False)
    location_info = LocationBunchSerializer(many=True, required=False)
    author = UserSerializer(read_only=True)
    author_info = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ['id', 'title', 'tour_images', 'amount_of_days', 'location_info', 'main_activity', 'main_location',
                  'difficulty_level', 'country', 'author', 'amount_of_days', 'author_info', 'concrete_tour_date']

    def get_author_info(self, obj):
        author = obj.author
        info = get_author_info(author)
        if info and 'image_url' in info and info['image_url']:
            request = self.context.get('request')
            info['image_url'] = request.build_absolute_uri(info['image_url']) if request else info['image_url']
        return info


class LocationInfoSerializer(serializers.ModelSerializer):
    location_info_images = LocationInfoImageSerializer(many=True, required=False)
    getting_there = GettingThereSerializer(many=True, required=False)

    country = CountryBunchSerializer(many=True, required=False)
    location = LocationBunchSerializer(many=True, required=False)
    collection = CollectionBunchSerializer(many=True, required=False)
    tourist_region = TouristRegionBunchSerializer(many=True, required=False)

    class Meta:
        model = LocationInfo
        fields = ('slug', 'title', 'short_description', 'description', 'how_to_get_there', 'coordinates',
                  'coordinates_map', 'location_info_images', 'getting_there',
                  'country', 'collection', 'location', 'tourist_region',)

    def create(self, validated_data):
        location_info_images_data = validated_data.pop('location_info_images', [])
        getting_there_data = validated_data.pop('getting_there', [])

        countries_data = validated_data.pop('country', [])
        locations_data = validated_data.pop('location', [])
        collections_data = validated_data.pop('collection', [])
        tourist_regions_data = validated_data.pop('tourist_region', [])

        location_info = LocationInfo.objects.create(**validated_data)

        location_info.collection.set([Collection.objects.get_or_create(**data)[0] for data in collections_data])
        location_info.country.set([Country.objects.get_or_create(**data)[0] for data in countries_data])
        location_info.location.set([Location.objects.get_or_create(**data)[0] for data in locations_data])
        location_info.tourist_region.set([TouristRegion.objects.get_or_create(**data)[0] for data in tourist_regions_data])

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

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.description = validated_data.get('description', instance.description)
        instance.how_to_get_there = validated_data.get('how_to_get_there', instance.how_to_get_there)
        instance.coordinates = validated_data.get('coordinates', instance.coordinates)
        instance.coordinates_map = validated_data.get('coordinates_map', instance.coordinates_map)
        instance.save()

        if 'country' in validated_data:
            countries = validated_data.pop('country')
            instance.country.set([Country.objects.get_or_create(**data)[0] for data in countries])

        if 'collection' in validated_data:
            collections = validated_data.pop('collection')
            instance.collection.set([Collection.objects.get_or_create(**data)[0] for data in collections])

        if 'location' in validated_data:
            locations = validated_data.pop('location')
            instance.location.set([Location.objects.get_or_create(**data)[0] for data in locations])

        if 'tourist_region' in validated_data:
            tourist_regions = validated_data.pop('tourist_region')
            instance.tourist_region.set([TouristRegion.objects.get_or_create(**data)[0] for data in tourist_regions])

        if 'location_info_images' in validated_data:
            location_info_images_data = validated_data.pop('location_info_images')
            instance.location_info_images.all().delete()
            for image_data in location_info_images_data:
                LocationInfoImage.objects.create(location_info=instance, **image_data)

        if 'getting_there' in validated_data:
            getting_there_data = validated_data.pop('getting_there')
            instance.getting_there.all().delete()
            for getting_data in getting_there_data:
                GettingThere.objects.create(location_info=instance, **getting_data)

        return instance
