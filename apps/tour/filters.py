from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as drf_filters
from django.db.models import Exists, OuterRef, Count
from django.db.models import Avg, Sum, Q


from apps.tour.models import Tour
from apps.tour.serializers import TourSerializer
from apps.concrete_tour.models import ConcreteTourDate


class CharFilterInFilter(drf_filters.BaseInFilter, drf_filters.CharFilter):
    pass


class KidAgeFilter(drf_filters.Filter):
    def filter(self, qs, value):
        if value in (None, '', 0):
            return qs
        return qs.filter(min_age__lte=value)


class MinRatingFilter(drf_filters.Filter):
    def filter(self, qs, value):
        if value in (None, ''):
            return qs
        qs = qs.annotate(average_rating=Avg('review__rating'))
        return qs.filter(average_rating__gte=value)


class PeopleCountFilter(drf_filters.Filter):
    def filter(self, qs, value):
        if value in (None, '', 0, '0'):
            return qs
        try:
            value = int(value)
        except ValueError:
            return qs
        return qs.annotate(
            available_dates=Exists(
                ConcreteTourDate.objects.filter(
                    tour_id=OuterRef('pk'),
                    total_seats_count__gte=value
                )
            )
        ).filter(available_dates=True)


class TourFilter(drf_filters.FilterSet):

    kid_age = KidAgeFilter(field_name='min_age')
    rating = MinRatingFilter(field_name='average_rating')
    amount_of_days = drf_filters.RangeFilter(field_name='amount_of_days')
    country = CharFilterInFilter(field_name='country__title', lookup_expr='in')
    language = CharFilterInFilter(field_name='language__title', lookup_expr='in')
    location = CharFilterInFilter(field_name='location__title', lookup_expr='in')
    price_KGZ = drf_filters.RangeFilter(field_name='concrete_tour_date__price_KGZ')
    type_tour = CharFilterInFilter(field_name='type_tour__title', lookup_expr='in')
    main_activity = CharFilterInFilter(field_name='main_activity', lookup_expr='in')
    main_location = CharFilterInFilter(field_name='main_location', lookup_expr='in')
    collection = CharFilterInFilter(field_name='collection__title', lookup_expr='in')
    people_count = PeopleCountFilter(field_name='concrete_tour_date__total_seats_count')
    comfort_level = CharFilterInFilter(field_name='comfort_level__title', lookup_expr='in')
    tourist_region = CharFilterInFilter(field_name='tourist_region__title', lookup_expr='in')
    difficulty_level = CharFilterInFilter(field_name='difficulty_level__title', lookup_expr='in')
    type_accommodation = CharFilterInFilter(field_name='place__place_residence__type_accommodation', lookup_expr='in')

    class Meta:
        model = Tour
        fields = [
            'price_KGZ', 'amount_of_days', 'type_accommodation', 'main_location', 'main_activity',
            'tourist_region', 'collection', 'difficulty_level', 'location', 'people_count', 'rating',
            'comfort_level', 'country', 'kid_age', 'type_tour', 'language',
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
        queryset = Tour.objects.all()

        ordering = self.request.query_params.get('ordering', '')

        if 'popular' in ordering:
            queryset = queryset.annotate(
                bookings_count=Count(
                    'concrete_tour_date__booking_tour',
                    filter=Q(concrete_tour_date__booking_tour__is_verified=True),
                    distinct=True
                )
            ).order_by('-bookings_count')
        elif 'high_rating' in ordering:
            queryset = queryset.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')
        else:
            pass

        queryset = self.filter_queryset(queryset)
        query = self.request.query_params.get('search', None)
        if query is not None:
            queryset = queryset.filter(title__icontains=query)

        return queryset.distinct()

