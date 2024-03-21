from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from django.http import Http404


from .permissions import IsOwner
from .models import Profile
from .serializers import (
    ProfileCreateSerializer,
    ProfileListSerializer,
    ProfileSerializer

)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    # serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileListSerializer
        elif self.action == 'create':
            return ProfileCreateSerializer
        elif self.action == 'retrieve':
            return ProfileSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return ProfileSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes in [IsOwner,IsAdminUser] # IsOwner, 
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [] # IsOwner, 
        return super().get_permissions()
