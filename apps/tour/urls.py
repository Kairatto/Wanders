from django.urls import path
from . import views

urlpatterns = [
    path('tour_create/', views.CreateTourWithDays.as_view(), name='tours'),
    path('tours/', views.TourList.as_view(), name='tour-list'),
    path('tours/<str:slug>/', views.TourDetail.as_view(), name='tour-detail'),
]
