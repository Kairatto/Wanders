from django.urls import path

from apps.favorites.views import FeaturedToursCreate, FeaturedToursList, FeaturedToursDetail


urlpatterns = [
    path('create/', FeaturedToursCreate.as_view(), name='favorite-create'),
    path('list/', FeaturedToursList.as_view(), name='favorite-list'),
    path('detail/<int:pk>/', FeaturedToursDetail.as_view(), name='favorite-detail'),
]

