from django.urls import path

from apps.location_info.views import LocationInfoCreate, LocationInfoDetail, LocationInfoList


urlpatterns = [
    path('create/', LocationInfoCreate.as_view(), name='location-create'),
    path('list/', LocationInfoList.as_view(), name='location-list'),
    path('<str:slug>/', LocationInfoDetail.as_view(), name='location-detail'),
]
