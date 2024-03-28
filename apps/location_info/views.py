from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.account.permissions import IsStaff
from apps.tour.models import Tour
from apps.tour.utils import BaseCreateAPIView

from apps.location_info.models import LocationInfo
from apps.location_info.serializers import LocationInfoSerializer, TourForLocationSerializer


class LocationInfoCreate(BaseCreateAPIView):
    permission_classes = IsStaff
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
                'location': [{'location': loc['title']} for loc in item['location']],
            }

            filtered_data.append(filtered_item)

        return Response(filtered_data)


class LocationInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsStaff
    queryset = LocationInfo.objects.all()
    serializer_class = LocationInfoSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsStaff()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        location_titles = instance.location.all().values_list('title', flat=True)
        tours_to_location = Tour.objects.filter(location__title__in=location_titles).distinct()[:3]

        tours_to_location_serializer = TourForLocationSerializer(tours_to_location, many=True, context={'request': request})
        response_data = serializer.data
        response_data['tours_to_location'] = tours_to_location_serializer.data

        return Response(response_data)
