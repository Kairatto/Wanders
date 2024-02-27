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
        fields = ('slug', 'id', 'tour_currency', )

    def validate_tour_currency(self, value):
        return validate_unique(TourCurrency, 'tour_currency', value)


class TypeTourSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeTour
        fields = ('slug', 'id', 'type_tour', )

    def validate_type_tour(self, value):
        return validate_unique(TypeTour, 'type_tour', value)


class ComfortLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComfortLevel
        fields = ('slug', 'id', 'comfort_level', )

    def validate_comfort_level(self, value):
        return validate_unique(ComfortLevel, 'comfort_level', value)


class DifficultyLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DifficultyLevel
        fields = ('slug', 'id', 'difficulty_level', )

    def validate_difficulty_level(self, value):
        return validate_unique(DifficultyLevel, 'difficulty_level', value)


class InsuranceConditionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceConditions
        fields = ('slug', 'id', 'insurance_conditions', )

    def validate_insurance_conditions(self, value):
        return validate_unique(InsuranceConditions, 'insurance_conditions', value)


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('slug', 'id', 'language', )

    def validate_language(self, value):
        return validate_unique(Language, 'language', value)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('slug', 'id', 'country', )

    def validate_country(self, value):
        return validate_unique(Country, 'country', value)


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('slug', 'id', 'collection', )

    def validate_collection(self, value):
        return validate_unique(Collection, 'collection', value)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('slug', 'id', 'location', )

    def validate_location(self, value):
        return validate_unique(Location, 'location', value)


class TouristRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TouristRegion
        fields = ('slug', 'id', 'region', )

    def validate_tourist_region(self, value):
        return validate_unique(TouristRegion, 'region', value)


class TypeTourBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeTour
        fields = ('type_tour', )


class ComfortLevelBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComfortLevel
        fields = ('comfort_level', )


class DifficultyLevelBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = DifficultyLevel
        fields = ('difficulty_level', )


class InsuranceConditionsBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceConditions
        fields = ('insurance_conditions', )


class LanguageBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('language', )


class TourCurrencyBunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourCurrency
        fields = ('tour_currency', )


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
