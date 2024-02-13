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
    price_KGZ = drf_filters.RangeFilter(field_name='concrete_tour__price_KGZ')

    type_accommodation = CharFilterInFilter(field_name='place__place_residence__type_accommodation', lookup_expr='in')
    main_location = CharFilterInFilter(field_name='main_location__main_location', lookup_expr='in')
    tourist_region = CharFilterInFilter(field_name='tourist_region__region', lookup_expr='in')
    collection = CharFilterInFilter(field_name='collection__collection', lookup_expr='in')
    difficulty_level = CharFilterInFilter(field_name='difficulty_level', lookup_expr='in')
    # activity = CharFilterInFilter(field_name='activity__activity', lookup_expr='in')
    location = CharFilterInFilter(field_name='location__location', lookup_expr='in')
    comfort_level = CharFilterInFilter(field_name='comfort_level', lookup_expr='in')
    country = CharFilterInFilter(field_name='country__country', lookup_expr='in')
    type_tour = CharFilterInFilter(field_name='type_tour', lookup_expr='in')
    language = CharFilterInFilter(field_name='language', lookup_expr='in')

    class Meta:
        model = Tour
        fields = [
            'price_KGZ', 'amount_of_days', 'type_accommodation', 'main_location',
            'tourist_region', 'collection', 'difficulty_level', 'location',
            'comfort_level', 'country', 'type_tour', 'language',
        ]


class CommonTourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['create_date', 'concrete_tour__price_KGZ']
    filterset_class = TourFilter

    def get_base_queryset(self):
        queryset = Tour.objects.filter(is_active=True)
        queryset = self.filter_queryset(queryset)
        return queryset

    def get_queryset(self):
        queryset = self.get_base_queryset()
        queryset = queryset.distinct()
        return queryset
