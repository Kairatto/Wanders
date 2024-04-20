from rest_framework import serializers
from .models import ConcreteTourDate, BookingTour
from ..guide.serializers import GuideCRMSerializer
from ..tour.models import Tour


class TourCRMSerializer(serializers.ModelSerializer):
    guide = GuideCRMSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('id', 'title', 'guide')


class ConcreteTourDateListSerializer(serializers.ModelSerializer):
    tour = TourCRMSerializer()

    class Meta:
        model = ConcreteTourDate
        fields = ('id', 'start_date', 'tour', 'price_KGZ')


class BookingTourCRMSerializer(serializers.ModelSerializer):
    concrete_tour_date = ConcreteTourDateListSerializer()

    class Meta:
        model = BookingTour
        fields = ('id', 'concrete_tour_date', 'is_verified', 'name', 'email', 'phone', 'seats_count', 'created')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        guide_data = instance.concrete_tour_date.tour.guide.values_list('first_name', flat=True)
        representation['concrete_tour_date']['tour']['guide'] = guide_data
        return representation


class ConcreteTourDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteTourDate
        fields = ('id', 'start_date', 'end_date', 'price_KGZ', 'amount_seat', 'total_seats_count')


class ConcreteTourDateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteTourDate
        fields = ('id', 'tour', 'start_date', 'end_date', 'price_KGZ', 'amount_seat')


class BookingTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTour
        fields = ('id', 'seats_count', 'concrete_tour_date', 'name', 'phone', 'email',
                  'description', 'is_verified', 'created')

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
