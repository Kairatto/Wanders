from django.urls import path

from .views import (
    DaysView,
    DaysRetrieveUpdateDeleteView
)


urlpatterns = [
    path('days/<str:slug>/', DaysRetrieveUpdateDeleteView.as_view(), name='day-retrieve'),
    path('days/', DaysView.as_view(), name='days'),

]
