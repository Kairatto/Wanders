from rest_framework import serializers
from django.db.models import Avg

from apps.tour.models import Tour
from apps.guide.models import Guide
from apps.question.models import Question
from apps.days.models import Days, DaysImage
from apps.tour.utils import get_author_info
from apps.tour_images.models import TourImages
from apps.list_of_things.models import ListOfThings
from apps.includes.models import Included, NotIncluded
from apps.concrete_tour.models import ConcreteTourDate
from apps.accommodation.models import (PlaceResidence, PlaceResidenceImages, Place)
from apps.tags.models import (Collection, Country, Location, TouristRegion, Language, TourCurrency)

from apps.tags.serializers import (CollectionBunchSerializer, CountryBunchSerializer, LocationBunchSerializer,
                                   TouristRegionBunchSerializer, LanguageBunchSerializer, TourCurrencyBunchSerializer)
from apps.includes.serializers import NotIncludedSerializer, IncludedSerializer
from apps.concrete_tour.serializers import ConcreteTourDateSerializer
from apps.list_of_things.serializers import ListOfThingsSerializer
from apps.tour_images.serializers import TourImagesSerializer
from apps.accommodation.serializers import PlaceSerializer
from apps.question.serializers import QuestionSerializer
from apps.guide.serializers import GuideBunchSerializer
from apps.review.serializers import ReviewSerializer
from apps.account.serializers import UserSerializer
from apps.days.serializers import DaysSerializer


class TourAuthorSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tour
        fields = ('id', 'title', 'author', 'create_date')


class SimilarTourSerializer(serializers.ModelSerializer):
    country = CountryBunchSerializer(many=True, required=False)
    concrete_tour_date = ConcreteTourDateSerializer(many=True, required=False)
    author = UserSerializer(read_only=True)
    author_info = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ['id', 'title', 'main_activity', 'main_location', 'difficulty_level',
                  'country', 'amount_of_days', 'author', 'author_info', 'concrete_tour_date']

    def get_author_info(self, obj):
        author = obj.author
        info = get_author_info(author)
        if info and 'image_url' in info and info['image_url']:
            request = self.context.get('request')
            info['image_url'] = request.build_absolute_uri(info['image_url']) if request else info['image_url']
        return info


class TourSerializer(serializers.ModelSerializer):
    list_of_things = ListOfThingsSerializer(many=True, required=False)
    concrete_tour_date = ConcreteTourDateSerializer(many=True, required=False)
    not_included = NotIncludedSerializer(many=True, required=False)
    tour_images = TourImagesSerializer(many=True, required=False)
    included = IncludedSerializer(many=True, required=False)
    question = QuestionSerializer(many=True, required=False)
    guide = GuideBunchSerializer(many=True, required=False)
    place = PlaceSerializer(many=True, required=False)
    days = DaysSerializer(many=True, required=False)

    country = CountryBunchSerializer(many=True, required=False)
    location = LocationBunchSerializer(many=True, required=False)
    collection = CollectionBunchSerializer(many=True, required=False)
    tourist_region = TouristRegionBunchSerializer(many=True, required=False)

    tour_currency = TourCurrencyBunchSerializer(many=True, required=False)
    language = LanguageBunchSerializer(many=True, required=False)

    author = UserSerializer(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    reviews_count = serializers.SerializerMethodField(read_only=True)
    author_info = serializers.SerializerMethodField(read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and 'people_count' in request.query_params:
            people_count_param = request.query_params['people_count']
            if people_count_param.isdigit():
                people_count = int(people_count_param)
                filtered_dates = [date for date in representation['concrete_tour_date'] if
                                  date['total_seats_count'] >= people_count]
                representation['concrete_tour_date'] = filtered_dates
            else:
                pass
        return representation

    class Meta:
        model = Tour
        fields = ('id', 'title', 'description', 'language', 'amount_of_days', 'min_people', 'max_people',
                  'min_age', 'max_age', 'difficulty_level', 'comfort_level', 'tour_currency', 'type_tour',
                  'insurance_conditions', 'tour_images', 'concrete_tour_date', 'list_of_things', 'included',
                  'not_included', 'days', 'place', 'guide', 'question', 'country', 'collection', 'main_activity',
                  'location', 'main_location', 'tourist_region', 'author', 'author_info',
                  'average_rating', 'reviews_count', 'reviews',
                  'is_active', 'is_draft', 'is_verified', 'is_archive', 'create_date')

    def get_author_info(self, obj):
        author = obj.author
        info = get_author_info(author)
        if info and 'image_url' in info and info['image_url']:
            request = self.context.get('request')
            info['image_url'] = request.build_absolute_uri(info['image_url']) if request else info['image_url']
        return info

    def get_average_rating(self, obj):
        average = obj.review_set.aggregate(Avg('rating')).get('rating__avg')
        if average is not None:
            return round(average, 1)
        return 0

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data

    def get_reviews_count(self, obj):
        return obj.review_set.count()

    def create(self, validated_data):
        concrete_tour_date_data = validated_data.pop('concrete_tour_date', [])
        list_of_things_data = validated_data.pop('list_of_things', [])
        not_included_data = validated_data.pop('not_included', [])
        tour_images_data = validated_data.pop('tour_images', [])
        questions_data = validated_data.pop('question', [])
        included_data = validated_data.pop('included', [])
        guide_data = validated_data.pop('guide', [])
        place_data = validated_data.pop('place', [])
        days_data = validated_data.pop('days', [])

        language_data = validated_data.pop('language', [])
        tour_currency_data = validated_data.pop('tour_currency', [])

        countries_data = validated_data.pop('country', [])
        locations_data = validated_data.pop('location', [])
        collections_data = validated_data.pop('collection', [])
        tourist_regions_data = validated_data.pop('tourist_region', [])

        tour = Tour.objects.create(**validated_data)

        tour.language.set([Language.objects.get_or_create(**data)[0] for data in language_data])
        tour.tour_currency.set([TourCurrency.objects.get_or_create(**data)[0] for data in tour_currency_data])

        tour.country.set([Country.objects.get_or_create(**data)[0] for data in countries_data])
        tour.location.set([Location.objects.get_or_create(**data)[0] for data in locations_data])
        tour.collection.set([Collection.objects.get_or_create(**data)[0] for data in collections_data])
        tour.tourist_region.set([TouristRegion.objects.get_or_create(**data)[0] for data in tourist_regions_data])

        tour.guide.set([Guide.objects.get_or_create(**data)[0] for data in guide_data])

        for languages_data in language_data:
            language, created = Language.objects.get_or_create(**languages_data)
            tour.language.add(language)

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

        for tour_image_data in tour_images_data:
            TourImages.objects.create(tour=tour, **tour_image_data)

        for concrete_tour_dates_data in concrete_tour_date_data:
            ConcreteTourDate.objects.create(tour=tour, **concrete_tour_dates_data)

        for day_data in days_data:
            days_images_data = day_data.pop('days_images', [])
            days = Days.objects.create(tour=tour, **day_data)

            for image_data in days_images_data:
                DaysImage.objects.create(day=days, **image_data)

        for places_data in place_data:
            place_residence_data = places_data.pop('place_residence', [])
            place = Place.objects.create(tour=tour, **places_data)

            for places_residence_data in place_residence_data:
                place_residence_images_data = places_residence_data.pop('place_residence_images', [])
                place_residence = PlaceResidence.objects.create(place=place, **places_residence_data)

                for places_residence_images_data in place_residence_images_data:
                    PlaceResidenceImages.objects.create(place_residence=place_residence, **places_residence_images_data)

        return tour

    def update(self, instance, validated_data):

        fields_to_clear_if_missing = [
            'title', 'description', 'amount_of_days', 'min_people', 'max_people',
            'min_age', 'max_age', 'difficulty_level', 'comfort_level', 'type_tour',
            'insurance_conditions', 'main_activity', 'main_location'
        ]

        simple_attrs = {attr: value for attr, value in validated_data.items() if attr not in [
            'list_of_things', 'concrete_tour_date', 'not_included', 'tour_images', 'included', 'question', 'guide',
            'place', 'days', 'language', 'tour_currency', 'country', 'collection', 'location', 'tourist_region'
        ]}

        for attr, value in simple_attrs.items():
            setattr(instance, attr, value)
        instance.save()

        m2m_fields_to_clear = [
            'language', 'tour_currency', 'country', 'collection',
            'location', 'tourist_region', 'guide'
        ]

        m2m_fields = {
            'guide': (Guide, validated_data.pop('guide', [])),
            'country': (Country, validated_data.pop('country', [])),
            'language': (Language, validated_data.pop('language', [])),
            'location': (Location, validated_data.pop('location', [])),
            'collection': (Collection, validated_data.pop('collection', [])),
            'tour_currency': (TourCurrency, validated_data.pop('tour_currency', [])),
            'tourist_region': (TouristRegion, validated_data.pop('tourist_region', [])),
        }

        for field in fields_to_clear_if_missing:
            if field not in validated_data:
                setattr(instance, field, None)

        for field in m2m_fields_to_clear:
            if field not in validated_data:
                getattr(instance, field).clear()

        instance.save()

        if 'list_of_things' in validated_data:
            lists_of_things_data = validated_data.pop('list_of_things')
            instance.list_of_things.all().delete()
            for lists_of_things_data_data in lists_of_things_data:
                ListOfThings.objects.create(**lists_of_things_data_data, tour=instance)

        if 'not_included' in validated_data:
            not_includes_data = validated_data.pop('not_included')
            instance.not_included.all().delete()
            for not_included_data_data in not_includes_data:
                NotIncluded.objects.create(**not_included_data_data, tour=instance)

        if 'included' in validated_data:
            includes_data = validated_data.pop('included')
            instance.included.all().delete()
            for included_data_data in includes_data:
                Included.objects.create(**included_data_data, tour=instance)

        if 'question' in validated_data:
            questions_data = validated_data.pop('question')
            instance.question.all().delete()
            for question_data in questions_data:
                Question.objects.create(**question_data, tour=instance)

        if 'days' in validated_data:
            days_data = validated_data.pop('days')
            instance.days.all().delete()

            for day_item in days_data:
                days_images_data = day_item.pop('days_images', [])
                day_instance = Days.objects.create(tour=instance, **day_item)

                for image_data in days_images_data:
                    DaysImage.objects.create(day=day_instance, **image_data)

        if 'place' in validated_data:
            place_data_list = validated_data.pop('place')

            instance.place.all().delete()

            for place_data in place_data_list:
                place_residence_data = place_data.pop('place_residence', [])
                place_instance = Place.objects.create(tour=instance, **place_data)

                for pr_data in place_residence_data:
                    place_residence_images_data = pr_data.pop('place_residence_images', [])
                    place_residence_instance = PlaceResidence.objects.create(place=place_instance, **pr_data)

                    for image_data in place_residence_images_data:
                        PlaceResidenceImages.objects.create(place_residence=place_residence_instance, **image_data)

        for field, (Model, data) in m2m_fields.items():
            if data:
                objs = [Model.objects.get_or_create(**item)[0] for item in data]
                getattr(instance, field).set(objs)

        return instance
