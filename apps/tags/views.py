from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.account.permissions import IsStaff
from apps.tour.utils import BaseCreateAPIView

from apps.tags.models import (Country, Collection, Location, TouristRegion, Language,
                              InsuranceConditions, DifficultyLevel, ComfortLevel, TypeTour, TourCurrency)

from apps.tags.serializers import (CollectionSerializer, LocationSerializer, TouristRegionSerializer, CountrySerializer,
                                   TourCurrencyBunchSerializer, CollectionBunchSerializer, LocationBunchSerializer,
                                   LanguageSerializer, InsuranceConditionsSerializer, DifficultyLevelSerializer,
                                   TouristRegionBunchSerializer, CountryBunchSerializer, LanguageBunchSerializer,
                                   ComfortLevelSerializer, TypeTourSerializer, TourCurrencySerializer,
                                   InsuranceConditionsBunchSerializer, DifficultyLevelBunchSerializer,
                                   ComfortLevelBunchSerializer, TypeTourBunchSerializer, )


class TourCurrencyCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = TourCurrencySerializer


class TourCurrencyList(generics.ListAPIView):
    queryset = TourCurrency.objects.all()
    serializer_class = TourCurrencySerializer


class TourCurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = TourCurrency.objects.all()
    serializer_class = TourCurrencyBunchSerializer
    lookup_field = 'slug'


class TypeTourCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = TypeTourSerializer


class TypeTourList(generics.ListAPIView):
    queryset = TypeTour.objects.all()
    serializer_class = TypeTourSerializer


class TypeTourDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = TypeTour.objects.all()
    serializer_class = TypeTourBunchSerializer
    lookup_field = 'slug'


class ComfortLevelCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = ComfortLevelSerializer


class ComfortLevelList(generics.ListAPIView):
    queryset = ComfortLevel.objects.all()
    serializer_class = ComfortLevelSerializer


class ComfortLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = ComfortLevel.objects.all()
    serializer_class = ComfortLevelBunchSerializer
    lookup_field = 'slug'


class DifficultyLevelCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = DifficultyLevelSerializer


class DifficultyLevelList(generics.ListAPIView):
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelSerializer


class DifficultyLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelBunchSerializer
    lookup_field = 'slug'


class InsuranceConditionsCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = InsuranceConditionsSerializer


class InsuranceConditionsList(generics.ListAPIView):
    queryset = InsuranceConditions.objects.all()
    serializer_class = InsuranceConditionsSerializer


class InsuranceConditionsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = InsuranceConditions.objects.all()
    serializer_class = InsuranceConditionsBunchSerializer
    lookup_field = 'slug'


class LanguageCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = LanguageSerializer


class LanguageList(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = Language.objects.all()
    serializer_class = LanguageBunchSerializer
    lookup_field = 'slug'


class CollectionCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = CollectionSerializer


class CollectionList(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = Collection.objects.all()
    serializer_class = CollectionBunchSerializer
    lookup_field = 'slug'


class CountryCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = CountrySerializer


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = Country.objects.all()
    serializer_class = CountryBunchSerializer
    lookup_field = 'slug'


class LocationCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = LocationSerializer


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = Location.objects.all()
    serializer_class = LocationBunchSerializer
    lookup_field = 'slug'


class TouristRegionCreate(BaseCreateAPIView):
    permission_classes = IsStaff
    serializer_class = TouristRegionSerializer


class TouristRegionList(generics.ListAPIView):
    queryset = TouristRegion.objects.all()
    serializer_class = TouristRegionSerializer


class TouristRegionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = TouristRegion.objects.all()
    serializer_class = TouristRegionBunchSerializer
    lookup_field = 'slug'


# language, insurance_conditions, difficulty_level, comfort_level, type_tour, tour_currency


class AllTagsView(APIView):
    def get(self, request, format=None):
        collections = Collection.objects.all()
        countries = Country.objects.all()
        tourist_regions = TouristRegion.objects.all()
        locations = Location.objects.all()

        language = Language.objects.all()
        insurance_conditions = InsuranceConditions.objects.all()
        difficulty_level = DifficultyLevel.objects.all()
        comfort_level = ComfortLevel.objects.all()
        type_tour = TypeTour.objects.all()
        tour_currency = TourCurrency.objects.all()

        collection_serializer = CollectionSerializer(collections, many=True)
        country_serializer = CountrySerializer(countries, many=True)
        tourist_region_serializer = TouristRegionSerializer(tourist_regions, many=True)
        location_serializer = LocationSerializer(locations, many=True)

        language_serializer = LanguageSerializer(language, many=True)
        insurance_conditions_serializer = InsuranceConditionsSerializer(insurance_conditions, many=True)
        difficulty_level_serializer = DifficultyLevelSerializer(difficulty_level, many=True)
        comfort_level_serializer = ComfortLevelSerializer(comfort_level, many=True)
        type_tour_serializer = TypeTourSerializer(type_tour, many=True)
        tour_currency_serializer = TourCurrencySerializer(tour_currency, many=True)

        all_tags_data = {
            'collection': collection_serializer.data,
            'country': country_serializer.data,
            'tourist_region': tourist_region_serializer.data,
            'location': location_serializer.data,

            'language': language_serializer.data,
            'tour_currency': tour_currency_serializer.data,

            'insurance_conditions': insurance_conditions_serializer.data,
            'difficulty_level': difficulty_level_serializer.data,
            'comfort_level': comfort_level_serializer.data,
            'type_tour': type_tour_serializer.data,
        }

        return Response(all_tags_data)
