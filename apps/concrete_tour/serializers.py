from rest_framework import serializers
from .models import ConcreteTourDate, BookingTour


class ConcreteTourDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteTourDate
        fields = ('id', 'tour', 'start_date', 'end_date', 'price_KGZ', 'amount_seat', 'total_seats_count')


class ConcreteTourDateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteTourDate
        fields = ('id', 'tour', 'start_date', 'end_date', 'price_KGZ', 'amount_seat')


class BookingTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTour
        fields = ('id', 'seats_count', 'concrete_tour_date', 'first_name',
                  'last_name', 'phone', 'email', 'is_verified', 'created')

    def validate(self, data):
        concrete_tour_date = data.get('concrete_tour_date')
        seats_count = data.get('seats_count')

        if concrete_tour_date and seats_count:
            available_seats = concrete_tour_date.total_seats_count

            if self.instance:
                available_seats += self.instance.seats_count

            if seats_count > available_seats:
                raise serializers.ValidationError("Недостаточно мест для выполнения заявки.")

        return data
