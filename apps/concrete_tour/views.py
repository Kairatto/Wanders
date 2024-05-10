from django.db.models import Sum
from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters import DateFromToRangeFilter
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend

from apps.account.permissions import IsStaff
from apps.tour.utils import BaseCreateAPIView

from apps.concrete_tour.models import BookingTour, ConcreteTourDate
from apps.concrete_tour.serializers import (BookingTourSerializer, ConcreteTourDateCreateSerializer,
                                            BookingTourCRMSerializer, ConcreteTourDateSerializer)


class TourIDFilter(filters.Filter):
    def filter(self, qs, value):
        if value in (None, ''):
            return qs
        return qs.filter(concrete_tour_date__tour__id=value)


class BookingCRMFilter(filters.FilterSet):
    tour_id = TourIDFilter(field_name='tour_id', )
    search_date = DateFromToRangeFilter(field_name='concrete_tour_date__start_date')

    class Meta:
        model = BookingTour
        fields = ['tour_id', 'search_date']


class BookingCRMView(generics.ListAPIView):
    queryset = BookingTour.objects.all()
    serializer_class = BookingTourCRMSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BookingCRMFilter
    ordering_fields = ['id', 'concrete_tour_date__start_date', 'paid']
    ordering = ['id']


class ConcreteTourDateCreate(BaseCreateAPIView):
    serializer_class = ConcreteTourDateCreateSerializer


class ConcreteTourDateList(generics.ListAPIView):
    queryset = ConcreteTourDate.objects.all()
    serializer_class = ConcreteTourDateCreateSerializer


class ConcreteTourDateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConcreteTourDate.objects.all()
    serializer_class = ConcreteTourDateSerializer


class BookingTourCreate(BaseCreateAPIView):
    serializer_class = BookingTourSerializer


class BookingTourList(generics.ListAPIView):
    queryset = BookingTour.objects.all()
    serializer_class = BookingTourSerializer


class BookingTourDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsStaff]
    queryset = BookingTour.objects.all()
    serializer_class = BookingTourSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsStaff()]

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if 'paid' in serializer.validated_data:
            if serializer.validated_data['paid'] and not instance.paid:
                available_seats = instance.concrete_tour_date.total_seats_count
                if instance.seats_count > available_seats:
                    raise ValidationError('Невозможно подтвердить заявку: недостаточно мест.')

        if 'concrete_tour_date' in serializer.validated_data:
            new_concrete_tour_date = serializer.validated_data['concrete_tour_date']
            old_concrete_tour_date = instance.concrete_tour_date

            if old_concrete_tour_date.id != new_concrete_tour_date.id and instance.paid:
                potential_new_total_seats = BookingTour.objects.filter(
                    concrete_tour_date=new_concrete_tour_date, paid=True
                ).aggregate(total_seats=Sum('seats_count'))['total_seats'] or 0

                potential_new_total_seats += instance.seats_count

                if potential_new_total_seats > new_concrete_tour_date.amount_seat:
                    raise ValidationError("Перевод заявки невозможен: на другой дате недостаточно мест.")

                with transaction.atomic():
                    old_total_seats = BookingTour.objects.filter(
                        concrete_tour_date=old_concrete_tour_date, paid=True
                    ).exclude(id=instance.id).aggregate(total_seats=Sum('seats_count'))['total_seats'] or 0
                    old_concrete_tour_date.total_seats_count = old_concrete_tour_date.amount_seat - old_total_seats
                    old_concrete_tour_date.save()

                    new_concrete_tour_date.total_seats_count = new_concrete_tour_date.amount_seat - potential_new_total_seats
                    new_concrete_tour_date.save()

        self.perform_update(serializer)
        return Response(serializer.data)
