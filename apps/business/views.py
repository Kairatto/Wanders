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

from apps.account.permissions import IsOwner, CreateProfile
from .models import TourAgent
from .serializers import (
    TourAgentCreateSerializer,
    TourAgentListSerializer,
    TourAgentSerializer,
    TourAgentUpdateSerializer,

)


class TourAgentListView(APIView):

    def get(self, request: Request):
        bus = TourAgent.objects.all()
        serializer = TourAgentListSerializer(bus, many=True)
        return Response(serializer.data)


class TourAgentCreateView(APIView):
    permission_classes = [CreateProfile, IsAuthenticated]

    def post(self, request):
        serializer = TourAgentCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Вы успешно создали бизнес-профиль',
                status=status.HTTP_201_CREATED
            )


class TourAgentDetailView(APIView):
    permission_classes = [IsOwner]

    def get_object(self, slug):
        try:
            return TourAgent.objects.get(slug=slug)
        except TourAgent.DoesNotExist:
            raise Http404

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsOwner()]

    def get(self, request, slug, *args, **kwargs):
        agent = self.get_object(slug)
        serializer = TourAgentSerializer(agent)
        return Response(serializer.data)

    def put(self, request, slug, *args, **kwargs):
        agent = self.get_object(slug)
        serializer = TourAgentUpdateSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, *args, **kwargs):
        agent = self.get_object(slug)
        agent.delete()
        return Response('Бизнес аккаунт успешно удален', status=status.HTTP_204_NO_CONTENT)
