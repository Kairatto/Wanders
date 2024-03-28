from django.urls import path

from apps.about_us.views import AboutUsCreate, AboutUsList, AboutUsDetail

urlpatterns = [
    path('create/', AboutUsCreate.as_view(), name='about_us-create'),
    path('list/', AboutUsList.as_view(), name='about_us-list'),
    path('detail/<int:pk>/', AboutUsDetail.as_view(), name='about_us-detail'),
    ]
