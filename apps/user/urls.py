from django.urls import path

from .views import ProfileCreateAPIView, ProfileListAPIView, ProfileDetailAPIView

urlpatterns = [
    path('create/', ProfileCreateAPIView.as_view(), name='profile-create'),
    path('list/', ProfileListAPIView.as_view(), name='profile-list'),
    path('detail/<str:email>/', ProfileDetailAPIView.as_view(), name='profile-detail'),
]
