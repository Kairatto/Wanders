from django.urls import path

from apps.tags.views import (CountryCreate, CountryDetail, CountryList,
                             LocationCreate, LocationDetail, LocationList,
                             CollectionCreate, CollectionDetail, CollectionList,
                             TouristRegionCreate, TouristRegionDetail, TouristRegionList,
                             LanguageCreate, LanguageDetail, LanguageList,
                             InsuranceConditionsCreate, InsuranceConditionsDetail, InsuranceConditionsList,
                             DifficultyLevelCreate, DifficultyLevelDetail, DifficultyLevelList,
                             ComfortLevelCreate, ComfortLevelDetail, ComfortLevelList,
                             TypeTourCreate, TypeTourDetail, TypeTourList,
                             TourCurrencyCreate, TourCurrencyDetail, TourCurrencyList,
                             AllTagsView)


urlpatterns = [
    path('tour_currency/create/', TourCurrencyCreate.as_view(), name='tour_currency-create'),
    path('tour_currency/list/', TourCurrencyList.as_view(), name='tour_currency-list'),
    path('tour_currency/<str:slug>/', TourCurrencyDetail.as_view(), name='tour_currency-detail'),

    path('type_tour/create/', TypeTourCreate.as_view(), name='type_tour-create'),
    path('type_tour/list/', TypeTourList.as_view(), name='type_tour-list'),
    path('type_tour/<str:slug>/', TypeTourDetail.as_view(), name='type_tour-detail'),

    path('comfort_level/create/', ComfortLevelCreate.as_view(), name='comfort_level-create'),
    path('comfort_level/list/', ComfortLevelList.as_view(), name='comfort_level-list'),
    path('comfort_level/<str:slug>/', ComfortLevelDetail.as_view(), name='comfort_level-detail'),

    path('difficulty_level/create/', DifficultyLevelCreate.as_view(), name='difficulty_level-create'),
    path('difficulty_level/list/', DifficultyLevelList.as_view(), name='difficulty_level-list'),
    path('difficulty_level/<str:slug>/', DifficultyLevelDetail.as_view(), name='difficulty_level-detail'),

    path('insure_condition/create/', InsuranceConditionsCreate.as_view(), name='insure_condition-create'),
    path('insure_condition/list/', InsuranceConditionsList.as_view(), name='insure_condition-list'),
    path('insure_condition/<str:slug>/', InsuranceConditionsDetail.as_view(), name='insure_condition-detail'),

    path('language/create/', LanguageCreate.as_view(), name='language-create'),
    path('language/list/', LanguageList.as_view(), name='language-list'),
    path('language/<str:slug>/', LanguageDetail.as_view(), name='language-detail'),

    path('collection/create/', CollectionCreate.as_view(), name='collection-create'),
    path('collection/list/', CollectionList.as_view(), name='collection-list'),
    path('collection/<str:slug>/', CollectionDetail.as_view(), name='collection-detail'),

    path('country/create/', CountryCreate.as_view(), name='country-create'),
    path('country/list/', CountryList.as_view(), name='country-list'),
    path('country/<str:slug>/', CountryDetail.as_view(), name='country-detail'),

    path('location/create/', LocationCreate.as_view(), name='location-create'),
    path('location/list/', LocationList.as_view(), name='location-list'),
    path('location/<str:slug>/', LocationDetail.as_view(), name='location-detail'),

    path('tourist_region/create/', TouristRegionCreate.as_view(), name='tourist_region_create'),
    path('tourist_region/list/', TouristRegionList.as_view(), name='activity-list'),
    path('tourist_region/<str:slug>/', TouristRegionDetail.as_view(), name='activity-detail'),

    path('all/', AllTagsView.as_view(), name='all_tags'),

    # path('activity_create/', ActivityCreate.as_view(), name='activity-create'),
    # path('activity_list/', ActivityList.as_view(), name='activity-list'),
    # path('activity/<str:slug>/', ActivityDetail.as_view(), name='activity-detail'),

    # path('main_location_create/', MainLocationCreate.as_view(), name='main-location-create'),
    # path('main_location_list/', MainLocationList.as_view(), name='main-location-list'),
    # path('main_location/<str:slug>/', MainLocationDetail.as_view(), name='main-location-detail'),
]
