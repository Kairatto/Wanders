from rest_framework import serializers

from apps.tags.models import Country, Collection, Location, TouristRegion


def validate_unique(model, field_name, value):

    existing_object = model.objects.filter(**{field_name: value}).first()
    if existing_object:
        raise serializers.ValidationError(f"Тег '{value}' уже существует.")
    return value


# class ActivitySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Activity
#         fields = ('slug', 'activity',)
#
#     def validate_activity(self, value):
#         return validate_unique(Activity, 'activity', value)


# class MainLocationSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MainLocation
#         fields = ('slug', 'main_location', )
#
#     def validate_city(self, value):
#         return validate_unique(MainLocation, 'main_location', value)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('slug', 'country', )

    def validate_country(self, value):
        return validate_unique(Country, 'country', value)


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('slug', 'collection', )

    def validate_collection(self, value):
        return validate_unique(Collection, 'collection', value)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('slug', 'location', )

    def validate_location(self, value):
        return validate_unique(Location, 'location', value)


class TouristRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TouristRegion
        fields = ('slug', 'region', )

    def validate_tourist_region(self, value):
        return validate_unique(TouristRegion, 'region', value)


# class ActivityBunchSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Activity
#         fields = ('slug', 'activity',)


# class MainLocationBunchSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MainLocation
#         fields = ('main_location', )


class CountryBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('country', )


class CollectionBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('collection', )


class LocationBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('location', )


class TouristRegionBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = TouristRegion
        fields = ('region', )
