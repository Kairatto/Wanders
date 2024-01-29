from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django_filters import rest_framework as drf_filters

from .models import Tour
from .serializers import TourSerializer


class TourCreate(APIView):
    def post(self, request, format=None):
        serializer = TourSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourFilter(drf_filters.FilterSet):
    amount_of_days = drf_filters.RangeFilter(field_name='amount_of_days')
    concrete_tour__price_KGZ = drf_filters.RangeFilter(field_name='concrete_tour__price_KGZ')
    min_age = drf_filters.RangeFilter(field_name='min_age')

    class Meta:
        model = Tour
        fields = {
            'type_tour': ['exact'],
            'activity__activity': ['exact'],
            'country__country': ['exact'],
            'collection__collection': ['exact'],
            'location__location': ['exact'],
            'tourist_region__region': ['exact'],
            'main_location__main_location': ['exact'],
            'place__place_residence__type_accommodation': ['exact'],
            'comfort_level': ['exact'],
            'difficulty_level': ['exact'],
            'language': ['exact'],

        }


class TourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [filters.OrderingFilter, drf_filters.DjangoFilterBackend]
    ordering_fields = ['create_date', 'concrete_tour__price_KGZ']
    filterset_class = TourFilter

    def get_queryset(self):
        queryset = Tour.objects.filter(is_active=True)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
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
                'main_location': [city['main_location'] for city in item['main_location']],
                'activity': [activity['activity'] for activity in item['activity']],
                'country': [country['country'] for country in item['country']],
                'collection': [collection['collection'] for collection in item['collection']],
                'location': [location['location'] for location in item['location']],
                'tourist_region': [region['region'] for region in item['tourist_region']],
                'price_KGZ': item['concrete_tour'][0]['price_KGZ'],
                'start_dates': [date['start_date'] for date in concrete_tour_dates],
            }

            filtered_data.append(filtered_item)

        return Response(filtered_data)


class TourListDev(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [filters.OrderingFilter, drf_filters.DjangoFilterBackend]
    ordering_fields = ['create_date', 'concrete_tour__price_KGZ']
    filterset_class = TourFilter

    def get_queryset(self):
        queryset = Tour.objects.filter(is_active=True)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        return Response(data)


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
    