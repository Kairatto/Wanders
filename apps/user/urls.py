from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ( 
    ProfileViewSet 
)


router = DefaultRouter()
router.register('', ProfileViewSet, 'profile')


urlpatterns = [ 

]

urlpatterns += router.urls
