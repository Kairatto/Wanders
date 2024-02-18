from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.tour.filters import CommonTourListView
from apps.tour.serializers import TourSerializer
from apps.tour.models import Tour


class TourCreate(APIView):
    def post(self, request, format=None):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            concrete_tour_dates = item['concrete_tour'][0]['concrete_tour_date']

            filtered_item = {
                'slug': item['slug'],
                'title': item['title'],
                'amount_of_days': item['amount_of_days'],
                'difficulty_level': item['difficulty_level'],
                'tour_images': [image['image'] for image in item['tour_images']],
                'main_location': item['main_location'],
                'main_activity': item['main_activity'],
                # 'activity': item['activity'],
                'country': item['country'],
                'collection': item['collection'],
                'location': item['location'],
                'tourist_region': item['tourist_region'],
                'price_KGZ': item['concrete_tour'][0]['price_KGZ'],
                'start_dates': [date['start_date'] for date in concrete_tour_dates],
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
    