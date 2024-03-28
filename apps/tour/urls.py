from django.urls import path

from apps.tour.views import TourCreate, TourListDev, TourListView, TourDetail


urlpatterns = [
    path('create/', TourCreate.as_view(), name='tour-create'),
    path('dev/', TourListDev.as_view(), name='tour-list-dev'),
    path('list/', TourListView.as_view(), name='tour-list'),
    path('detail/<str:slug>/', TourDetail.as_view(), name='tour-detail'),
]
