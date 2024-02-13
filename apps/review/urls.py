from django.urls import path

from apps.review.views import (ReviewCreate, ReviewList, ReviewDetail)


urlpatterns = [
    path('create/', ReviewCreate.as_view(), name='review-create'),
    path('list/', ReviewList.as_view(), name='review-list'),
    path('detail/<str:slug>/', ReviewDetail.as_view(), name='review-detail'),
]
