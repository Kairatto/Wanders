from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Tour
from .serializers import TourSerializer


class TourCreate(APIView):
    def post(self, request, format=None):
        serializer = TourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourListDev(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_queryset(self):
        return Tour.objects.filter(is_active=True)


class TourListView(generics.ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        return Tour.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        filtered_data = []
        for item in data:
            filtered_item = {
                'slug': item['slug'],
                'title': item['title'],
                'amount_of_days': item['amount_of_days'],
                'difficulty_level': item['difficulty_level'],
                'city': [city['city'] for city in item['city']],
                'activity': [activity['activity'] for activity in item['activity']],
                'country': [country['country'] for country in item['country']],
                'collection': [collection['collection'] for collection in item['collection']],
                'location': [location['location'] for location in item['location']],
                'tourist_region': [region['region'] for region in item['tourist_region']],
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
    