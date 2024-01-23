from django.urls import path

from apps.tags.views import (CityCreate, CityDetail, CityList,
                             CountryCreate, CountryDetail, CountryList,
                             ActivityCreate, ActivityDetail, ActivityList,
                             LocationCreate, LocationDetail, LocationList,
                             CollectionCreate, CollectionDetail, CollectionList,
                             TouristRegionCreate, TouristRegionDetail, TouristRegionList)


urlpatterns = [
    path('city_create/', CityCreate.as_view(), name='city-create'),
    path('city_list/', CityList.as_view(), name='city-list'),
    path('city/<str:slug>/', CityDetail.as_view(), name='city-detail'),

    path('collection_create/', CollectionCreate.as_view(), name='collection-create'),
    path('collection_list/', CollectionList.as_view(), name='collection-list'),
    path('collection/<str:slug>/', CollectionDetail.as_view(), name='collection-detail'),

    path('country_create/', CountryCreate.as_view(), name='country-create'),
    path('country_list/', CountryList.as_view(), name='country-list'),
    path('country/<str:slug>/', CountryDetail.as_view(), name='country-detail'),

    path('location_create/', LocationCreate.as_view(), name='location-create'),
    path('location_list/', LocationList.as_view(), name='location-list'),
    path('location/<str:slug>/', LocationDetail.as_view(), name='location-detail'),

    path('activity_create/', ActivityCreate.as_view(), name='activity-create'),
    path('activity_list/', ActivityList.as_view(), name='activity-list'),
    path('activity/<str:slug>/', ActivityDetail.as_view(), name='activity-detail'),

    path('tourist_region_create/', TouristRegionCreate.as_view(), name='tourist_region_create'),
    path('tourist_region_list/', TouristRegionList.as_view(), name='activity-list'),
    path('tourist_region/<str:slug>/', TouristRegionDetail.as_view(), name='activity-detail'),
]
