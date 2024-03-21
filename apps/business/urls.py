from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ( 
    TourAgentCreateView, 
    TourAgentListView, 
    TourAgentRetrieveView, 
    TourAgentDeleteView,

    TourAgentViewSet 
)

#
# router = DefaultRouter()
# router.register('', TourAgentViewSet, 'tour_agents')


urlpatterns = [ 
    path('create/', TourAgentCreateView.as_view(), name='creation'),
    path('list/', TourAgentListView.as_view(), name='list'),
    path('<str:slug>/', TourAgentRetrieveView.as_view(), name='get_tour_gent'),
    path('delete/<str:slug>/', TourAgentDeleteView.as_view(), name='delete_tour_agent'),
]

# urlpatterns += router.urls
