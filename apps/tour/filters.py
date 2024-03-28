from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as drf_filters, Filter

from .models import Tour
from .serializers import TourSerializer


class CharFilterInFilter(drf_filters.BaseInFilter, drf_filters.CharFilter):
    pass


class TourFilter(drf_filters.FilterSet):

    # min_age = drf_filters.RangeFilter(field_name='min_age')
    amount_of_days = drf_filters.RangeFilter(field_name='amount_of_days')
    price_KGZ = drf_filters.RangeFilter(field_name='concrete_tour_date__price_KGZ')

    type_accommodation = CharFilterInFilter(field_name='place__place_residence__type_accommodation', lookup_expr='in')
    tourist_region = CharFilterInFilter(field_name='tourist_region__title', lookup_expr='in')
    collection = CharFilterInFilter(field_name='collection__title', lookup_expr='in')
    difficulty_level = CharFilterInFilter(field_name='difficulty_level__title', lookup_expr='in')
    location = CharFilterInFilter(field_name='location__title', lookup_expr='in')
    main_activity = CharFilterInFilter(field_name='main_activity', lookup_expr='in')
    comfort_level = CharFilterInFilter(field_name='comfort_level__title', lookup_expr='in')
    main_location = CharFilterInFilter(field_name='main_location', lookup_expr='in')
    country = CharFilterInFilter(field_name='country__title', lookup_expr='in')
    type_tour = CharFilterInFilter(field_name='type_tour__title', lookup_expr='in')
    language = CharFilterInFilter(field_name='language__title', lookup_expr='in')

    class Meta:
        model = Tour
        fields = [
            'price_KGZ', 'amount_of_days', 'type_accommodation', 'main_location', 'main_activity',
            'tourist_region', 'collection', 'difficulty_level', 'location',
            'comfort_level', 'country', 'type_tour', 'language',
        ]


class CommonTourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['create_date', 'concrete_tour_date__price_KGZ']
    filterset_class = TourFilter

    def get_base_queryset(self):
        queryset = Tour.objects
        return queryset

    def get_queryset(self):
        queryset = self.get_base_queryset()
        queryset = self.filter_queryset(queryset)
        query = self.request.query_params.get('search', None)

        if query is not None:
            queryset = queryset.filter(title__icontains=query)

        return queryset.distinct()
