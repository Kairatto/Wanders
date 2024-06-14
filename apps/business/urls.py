from django.urls import path

from .views import ( 
    TourAgentCreateView, 
    TourAgentListView, 
    TourAgentDetailView,

)


urlpatterns = [ 
    path('create/', TourAgentCreateView.as_view(), name='creation'),
    path('list/', TourAgentListView.as_view(), name='list'),
    path('detail/<str:email>/', TourAgentDetailView.as_view(), name='detail_tour_agent'),
]
