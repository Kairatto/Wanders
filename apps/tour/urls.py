from django.urls import path

from apps.tour.views import TourCreate, TourListDev, TourListView, TourDetail

urlpatterns = [
    path('tour_create/', TourCreate.as_view(), name='tours'),
    path('tours_dev/', TourListDev.as_view(), name='tour-list-dev'),
    path('tours/', TourListView.as_view(), name='tour-list'),
    path('tours/<str:slug>/', TourDetail.as_view(), name='tour-detail'),
]
