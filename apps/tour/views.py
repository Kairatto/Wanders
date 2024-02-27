from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.tour.filters import CommonTourListView
from apps.tour.serializers import TourSerializer
from apps.tour.models import Tour
from apps.tour.utils import BaseCreateAPIView


class TourCreate(BaseCreateAPIView):
    serializer_class = TourSerializer


class TourListDev(CommonTourListView):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class TourListView(CommonTourListView):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        filtered_data = []
        for item in data:

            filtered_item = {
                'slug': item['slug'],
                'title': item['title'],
                'amount_of_days': item['amount_of_days'],
                'difficulty_level': item['difficulty_level'],
                'tour_images': [image['image'] for image in item['tour_images']],
                'main_location': item['main_location'],
                'main_activity': item['main_activity'],
                'country': item['country'],
                'collection': item['collection'],
                'location': item['location'],
                'tourist_region': item['tourist_region'],
                'concrete_tour': item['concrete_tour'],
            }

            filtered_data.append(filtered_item)

        return Response(filtered_data)


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
    