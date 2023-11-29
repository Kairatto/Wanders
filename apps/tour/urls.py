from django.urls import path

from apps.tour.views import TourCreate, TourList, TourDetail

urlpatterns = [
    path('tour_create/', TourCreate.as_view(), name='tours'),
    path('tours/', TourList.as_view(), name='tour-list'),
    path('tours/<str:slug>/', TourDetail.as_view(), name='tour-detail'),
]
