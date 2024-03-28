from django.urls import path

from apps.location_info.views import LocationInfoCreate, LocationInfoDetail, LocationInfoList, LocationInfoDevList


urlpatterns = [
    path('create/', LocationInfoCreate.as_view(), name='location-create'),
    path('list/', LocationInfoList.as_view(), name='location-list'),
    path('dev/', LocationInfoDevList.as_view(), name='location-list-dev'),
    path('detail/<str:slug>/', LocationInfoDetail.as_view(), name='location-detail'),
]
