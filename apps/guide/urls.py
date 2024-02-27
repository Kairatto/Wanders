from django.urls import path

from apps.guide.views import GuideCreate, GuideList, GuideDetail


urlpatterns = [
    path('create/', GuideCreate.as_view(), name='guide-create'),
    path('list/', GuideList.as_view(), name='guide-list'),
    path('<str:slug>/', GuideDetail.as_view(), name='guide-detail'),
]

