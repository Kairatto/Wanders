from django.urls import path

from .views import TourList


urlpatterns = [
    path('tours/', TourList.as_view(), name='tour-list'),
]
