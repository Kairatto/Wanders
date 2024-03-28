from django.db import transaction
from django.db.models import Sum
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from apps.account.permissions import IsStaff
from apps.tour.utils import BaseCreateAPIView

from apps.concrete_tour.models import BookingTour, ConcreteTourDate
from apps.concrete_tour.serializers import BookingTourSerializer, ConcreteTourDateCreateSerializer


class ConcreteTourDateCreate(BaseCreateAPIView):
    serializer_class = ConcreteTourDateCreateSerializer


class ConcreteTourDateList(generics.ListAPIView):
    queryset = ConcreteTourDate.objects.all()
    serializer_class = ConcreteTourDateCreateSerializer


class BookingTourCreate(BaseCreateAPIView):
    serializer_class = BookingTourSerializer


class BookingTourList(generics.ListAPIView):
    queryset = BookingTour.objects.all()
    serializer_class = BookingTourSerializer


class BookingTourDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaff]
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

        if 'is_verified' in serializer.validated_data:
            if serializer.validated_data['is_verified'] and not instance.is_verified:
                available_seats = instance.concrete_tour_date.total_seats_count
                if instance.seats_count > available_seats:
                    raise ValidationError('Невозможно подтвердить заявку: недостаточно мест.')

        with transaction.atomic():
            if 'concrete_tour_date' in serializer.validated_data and instance.is_verified:
                old_concrete_tour_date = instance.concrete_tour_date
                new_concrete_tour_date = serializer.validated_data['concrete_tour_date']

                if old_concrete_tour_date.id != new_concrete_tour_date.id:
                    potential_old_total_seats = BookingTour.objects.filter(
                        concrete_tour_date=old_concrete_tour_date,
                        is_verified=True
                    ).exclude(id=instance.id).aggregate(total_seats=Sum('seats_count'))['total_seats'] or 0

                    potential_new_total_seats = BookingTour.objects.filter(
                        concrete_tour_date=new_concrete_tour_date,
                        is_verified=True
                    ).aggregate(total_seats=Sum('seats_count'))['total_seats'] or 0 + instance.seats_count

                    if potential_old_total_seats > old_concrete_tour_date.amount_seat or \
                            potential_new_total_seats > new_concrete_tour_date.amount_seat:
                        raise ValidationError("Перевод заявки приведет к недопустимому количеству мест.")

                    old_concrete_tour_date.total_seats_count = old_concrete_tour_date.amount_seat - potential_old_total_seats
                    old_concrete_tour_date.save()

                    new_concrete_tour_date.total_seats_count = new_concrete_tour_date.amount_seat - potential_new_total_seats
                    new_concrete_tour_date.save()

            self.perform_update(serializer)
            return Response(serializer.data)

