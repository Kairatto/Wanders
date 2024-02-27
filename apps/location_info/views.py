from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.tour.utils import BaseCreateAPIView

from .models import LocationInfo
from .serializers import LocationInfoSerializer


class LocationInfoCreate(BaseCreateAPIView):
    serializer_class = LocationInfoSerializer


class LocationInfoDevList(generics.ListAPIView):
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']


class LocationInfoList(generics.ListAPIView):
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        filtered_data = []
        for item in data:
            filtered_item = {
                'slug': item['slug'],
                'title': item['title'],
                'location_info_images': item['location_info_images'],
                'location': [{'location': loc['location']} for loc in item['location']],
            }

            filtered_data.append(filtered_item)

        return Response(filtered_data)


class LocationInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer
    lookup_field = 'slug'
