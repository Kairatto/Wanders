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
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .permissions import IsOwner
from .models import TourAgent
from .serializers import (
    TourAgentCreateSerializer,
    TourAgentListSerializer,
    TourAgentSerializer,
    TourAgentUpdateSerializer,

)


class TourAgentListView(APIView):
    # search_fields = ['title']

    def get(self, request: Request):
        bus = TourAgent.objects.all()
        serializer = TourAgentListSerializer(bus, many=True)
        return Response(serializer.data)


class TourAgentCreateView(APIView):
    def post(self, request: Request):
        serializer = TourAgentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(
                'Вы успешно создали бизнес-профиль',
                status=status.HTTP_201_CREATED
            )


class TourAgentRetrieveView(APIView):
    def get(self, request, slug):
        try:
            bus = TourAgent.objects.filter(slug=slug)
            serializer = TourAgentSerializer(bus, many=True).data
            return Response(serializer)
        except TourAgent.DoesNotExist:
            raise Http404


class TourAgentDeleteView(APIView):
    permission_classes = [IsOwner]

    def delete(self, request: Request, slug):
        profile = TourAgent.objects.get(slug=slug)
        profile.delete()
        return Response(
            'Ваш бизнес профиль удален.',
            status=status.HTTP_204_NO_CONTENT
        )


class TourAgentViewSet(ModelViewSet):
    queryset = TourAgent.objects.all()
    serializer_class = TourAgentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def check_businessprofile(self, request):
    #     serializer = TourAgentCreateSerializer(
    #             data=request.data, 
    #             context={
    #                 'request':request,
    #             })

    def get_serializer_class(self):
        if self.action == 'list':
            return TourAgentListSerializer
        elif self.action == 'create':
            return TourAgentCreateSerializer
        elif self.action == 'retrieve':
            return TourAgentSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return TourAgentUpdateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes in [IsOwner, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()
