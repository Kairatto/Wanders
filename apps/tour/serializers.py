from rest_framework import serializers

from apps.account.serializers import UserSerializer
from apps.tour.models import Tour
from apps.guide.models import Guide
from apps.question.models import Question
from apps.days.models import Days, DaysImage
from apps.tour_images.models import TourImages
from apps.list_of_things.models import ListOfThings
from apps.includes.models import Included, NotIncluded
from apps.recommendations.models import Recommendations
from apps.collection_point.models import CollectionPoint
from apps.concrete_tour.models import ConcreteTour, ConcreteTourDate
from apps.accommodation.models import (PlaceResidence, PlaceResidenceImages, Place)
from apps.tags.models import (Collection, Country, Location, TouristRegion, Language,
                              InsuranceConditions, DifficultyLevel, ComfortLevel, TypeTour, TourCurrency)

from apps.tags.serializers import (CollectionBunchSerializer, CountryBunchSerializer, LocationBunchSerializer,
                                   TouristRegionBunchSerializer, LanguageBunchSerializer,
                                   InsuranceConditionsBunchSerializer, DifficultyLevelBunchSerializer,
                                   ComfortLevelBunchSerializer, TypeTourBunchSerializer, TourCurrencyBunchSerializer)
from apps.includes.serializers import NotIncludedSerializer, IncludedSerializer
from apps.collection_point.serializers import CollectionPointSerializer
from apps.recommendations.serializers import RecommendationsSerializer
from apps.list_of_things.serializers import ListOfThingsSerializer
from apps.concrete_tour.serializers import ConcreteTourSerializer
from apps.tour_images.serializers import TourImagesSerializer
from apps.accommodation.serializers import PlaceSerializer
from apps.question.serializers import QuestionSerializer
from apps.guide.serializers import GuideBunchSerializer
from apps.days.serializers import DaysSerializer


class SimilarTourSerializer(serializers.ModelSerializer):
    country = CountryBunchSerializer(many=True, required=False)
    concrete_tour = ConcreteTourSerializer(many=True, required=False)

    class Meta:
        model = Tour
        fields = ['slug', 'main_activity', 'main_location', 'difficulty_level', 'country', 'amount_of_days', 'concrete_tour']


class TourSerializer(serializers.ModelSerializer):
    collection_point = CollectionPointSerializer(many=True, required=False)
    recommendations = RecommendationsSerializer(many=True, required=False)
    list_of_things = ListOfThingsSerializer(many=True, required=False)
    concrete_tour = ConcreteTourSerializer(many=True, required=False)
    not_included = NotIncludedSerializer(many=True, required=False)
    tour_images = TourImagesSerializer(many=True, required=False)
    included = IncludedSerializer(many=True, required=False)
    question = QuestionSerializer(many=True, required=False)
    guide = GuideBunchSerializer(many=True, required=False)
    place = PlaceSerializer(many=True, required=False)
    days = DaysSerializer(many=True, required=False)

    tourist_region = TouristRegionBunchSerializer(many=True, required=False)
    collection = CollectionBunchSerializer(many=True, required=False)
    location = LocationBunchSerializer(many=True, required=False)
    country = CountryBunchSerializer(many=True, required=False)

    language = LanguageBunchSerializer(many=True, required=False)
    tour_currency = TourCurrencyBunchSerializer(many=True, required=False)

    author = UserSerializer(read_only=True)

    # insurance_conditions = InsuranceConditionsBunchSerializer(many=True, required=False)
    # difficulty_level = DifficultyLevelBunchSerializer(many=True, required=False)
    # comfort_level = ComfortLevelBunchSerializer(many=True, required=False)
    # type_tour = TypeTourBunchSerializer(many=True, required=False)

    class Meta:
        model = Tour
        fields = ('slug', 'title', 'description', 'language', 'amount_of_days', 'min_people', 'max_people',
                  'min_age', 'max_age', 'difficulty_level', 'comfort_level', 'tour_currency', 'type_tour',
                  'insurance_conditions', 'tour_images', 'concrete_tour', 'collection_point',
                  'recommendations', 'list_of_things', 'included', 'not_included', 'days', 'place',
                  'guide', 'question', 'country', 'collection', 'main_activity', 'location', 'main_location',
                  'tourist_region', 'author', 'is_active', 'create_date')

    def create(self, validated_data):
        collection_point_data = validated_data.pop('collection_point', [])
        recommendations_data = validated_data.pop('recommendations', [])
        list_of_things_data = validated_data.pop('list_of_things', [])
        concrete_tour_data = validated_data.pop('concrete_tour', [])
        not_included_data = validated_data.pop('not_included', [])
        tour_images_data = validated_data.pop('tour_images', [])
        questions_data = validated_data.pop('question', [])
        included_data = validated_data.pop('included', [])
        guide_data = validated_data.pop('guide', [])
        place_data = validated_data.pop('place', [])
        days_data = validated_data.pop('days', [])

        language_data = validated_data.pop('language', [])
        tour_currency_data = validated_data.pop('tour_currency', [])
        # insurance_conditions_data = validated_data.pop('insurance_conditions', [])
        # difficulty_level_data = validated_data.pop('difficulty_level', [])
        # comfort_level_data = validated_data.pop('comfort_level', [])
        # type_tour_data = validated_data.pop('type_tour', [])

        countries_data = validated_data.pop('country', [])
        locations_data = validated_data.pop('location', [])
        collections_data = validated_data.pop('collection', [])
        tourist_regions_data = validated_data.pop('tourist_region', [])

        tour = Tour.objects.create(**validated_data)

        tour.language.set([Language.objects.get_or_create(**data)[0] for data in language_data])
        tour.tour_currency.set([TourCurrency.objects.get_or_create(**data)[0] for data in tour_currency_data])
        # tour.insurance_conditions.set([InsuranceConditions.objects.get_or_create(**data)[0] for data in insurance_conditions_data])
        # tour.difficulty_level.set([DifficultyLevel.objects.get_or_create(**data)[0] for data in difficulty_level_data])
        # tour.comfort_level.set([ComfortLevel.objects.get_or_create(**data)[0] for data in comfort_level_data])
        # tour.type_tour.set([TypeTour.objects.get_or_create(**data)[0] for data in type_tour_data])

        tour.country.set([Country.objects.get_or_create(**data)[0] for data in countries_data])
        tour.location.set([Location.objects.get_or_create(**data)[0] for data in locations_data])
        tour.collection.set([Collection.objects.get_or_create(**data)[0] for data in collections_data])
        tour.tourist_region.set([TouristRegion.objects.get_or_create(**data)[0] for data in tourist_regions_data])

        tour.guide.set([Guide.objects.get_or_create(**data)[0] for data in guide_data])

        for languages_data in language_data:
            language, created = Language.objects.get_or_create(**languages_data)
            tour.language.add(language)

        # for insurance_condition_data in insurance_conditions_data:
        #     insurance_conditions, created = InsuranceConditions.objects.get_or_create(**insurance_condition_data)
        #     tour.insurance_conditions.add(insurance_conditions)
        #
        # for difficulty_levels_data in difficulty_level_data:
        #     difficulty_level, created = DifficultyLevel.objects.get_or_create(**difficulty_levels_data)
        #     tour.difficulty_level.add(difficulty_level)
        #
        # for comfort_levels_data in comfort_level_data:
        #     comfort_level, created = ComfortLevel.objects.get_or_create(**comfort_levels_data)
        #     tour.comfort_level.add(comfort_level)
        #
        # for type_tours_data in type_tour_data:
        #     type_tour, created = TypeTour.objects.get_or_create(**type_tours_data)
        #     tour.type_tour.add(type_tour)

        for guides_data in guide_data:
            guide, created = Guide.objects.get_or_create(**guides_data)
            tour.guide.add(guide)

        for tours_currency_data in tour_currency_data:
            tour_currency, created = TourCurrency.objects.get_or_create(**tours_currency_data)
            tour.tour_currency.add(tour_currency)

        for collection_data in collections_data:
            collection, created = Collection.objects.get_or_create(**collection_data)
            tour.collection.add(collection)

        for country_data in countries_data:
            country, created = Country.objects.get_or_create(**country_data)
            tour.country.add(country)

        for location_data in locations_data:
            location, created = Location.objects.get_or_create(**location_data)
            tour.location.add(location)

        for tourist_region_data in tourist_regions_data:
            tourist_region, created = TouristRegion.objects.get_or_create(**tourist_region_data)
            tour.tourist_region.add(tourist_region)

        for not_includes_data in not_included_data:
            NotIncluded.objects.create(tour=tour, **not_includes_data)

        for includes_data in included_data:
            Included.objects.create(tour=tour, **includes_data)

        for question_data in questions_data:
            Question.objects.create(tour=tour, **question_data)

        for list_of_thing_data in list_of_things_data:
            ListOfThings.objects.create(tour=tour, **list_of_thing_data)

        for recommendation_data in recommendations_data:
            Recommendations.objects.create(tour=tour, **recommendation_data)

        for tour_image_data in tour_images_data:
            TourImages.objects.create(tour=tour, **tour_image_data)

        for collection_points_data in collection_point_data:
            tourist_region_data = collection_points_data.pop('tourist_region', [])
            collection_point = CollectionPoint.objects.create(tour=tour, **collection_points_data)
            collection_point.tourist_region.set(
                [TouristRegion.objects.get_or_create(**data)[0] for data in tourist_region_data])

        for day_data in days_data:
            days_images_data = day_data.pop('days_images', [])
            days = Days.objects.create(tour=tour, **day_data)

            for image_data in days_images_data:
                DaysImage.objects.create(day=days, **image_data)

        for concrete_tours_data in concrete_tour_data:
            concrete_tour_date_data = concrete_tours_data.pop('concrete_tour_date', [])
            concrete_tour = ConcreteTour.objects.create(tour=tour, **concrete_tours_data)

            for concrete_tours_date_data in concrete_tour_date_data:
                ConcreteTourDate.objects.create(concrete_tour=concrete_tour, **concrete_tours_date_data)

        for places_data in place_data:
            place_residence_data = places_data.pop('place_residence', [])
            place = Place.objects.create(tour=tour, **places_data)

            for places_residence_data in place_residence_data:
                place_residence_images_data = places_residence_data.pop('place_residence_images', [])
                place_residence = PlaceResidence.objects.create(place=place, **places_residence_data)

                for places_residence_images_data in place_residence_images_data:
                    PlaceResidenceImages.objects.create(place_residence=place_residence, **places_residence_images_data)

        return tour


