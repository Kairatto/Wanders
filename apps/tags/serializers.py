from rest_framework import serializers

from apps.tags.models import (Country, Collection, Location, TouristRegion, Language,
                              InsuranceConditions, DifficultyLevel, ComfortLevel, TypeTour, TourCurrency)


def validate_unique(model, field_name, value):

    existing_object = model.objects.filter(**{field_name: value}).first()
    if existing_object:
        raise serializers.ValidationError(f"Тег '{value}' уже существует.")
    return value


class TourCurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = TourCurrency
        fields = ('slug', 'id', 'title', )

    def validate_tour_currency(self, value):
        return validate_unique(TourCurrency, 'title', value)


class TypeTourSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeTour
        fields = ('slug', 'id', 'title', )

    def validate_type_tour(self, value):
        return validate_unique(TypeTour, 'title', value)


class ComfortLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComfortLevel
        fields = ('slug', 'id', 'title', )

    def validate_comfort_level(self, value):
        return validate_unique(ComfortLevel, 'title', value)


class DifficultyLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DifficultyLevel
        fields = ('slug', 'id', 'title', )

    def validate_difficulty_level(self, value):
        return validate_unique(DifficultyLevel, 'title', value)


class InsuranceConditionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceConditions
        fields = ('slug', 'id', 'title', )

    def validate_insurance_conditions(self, value):
        return validate_unique(InsuranceConditions, 'title', value)


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('slug', 'id', 'title', )

    def validate_language(self, value):
        return validate_unique(Language, 'title', value)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('slug', 'id', 'title', )

    def validate_country(self, value):
        return validate_unique(Country, 'title', value)


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('slug', 'id', 'title', )

    def validate_collection(self, value):
        return validate_unique(Collection, 'title', value)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('slug', 'id', 'title', )

    def validate_location(self, value):
        return validate_unique(Location, 'title', value)


class TouristRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TouristRegion
        fields = ('slug', 'id', 'title', )

    def validate_tourist_region(self, value):
        return validate_unique(TouristRegion, 'title', value)


class TypeTourBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeTour
        fields = ('title', )


class ComfortLevelBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComfortLevel
        fields = ('title', )


class DifficultyLevelBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = DifficultyLevel
        fields = ('title', )


class InsuranceConditionsBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceConditions
        fields = ('title', )


class LanguageBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('title', )


class TourCurrencyBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourCurrency
        fields = ('title', )


class CountryBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('title', )


class CollectionBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('title', )


class LocationBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('title', )


class TouristRegionBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = TouristRegion
        fields = ('title', )


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
