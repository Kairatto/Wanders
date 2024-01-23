from rest_framework import serializers
from .models import ConcreteTourDate, ConcreteTour


class ConcreteTourDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcreteTourDate
        fields = ('start_date', 'end_date', 'amount_seat')


class ConcreteTourSerializer(serializers.ModelSerializer):
    concrete_tour_date = ConcreteTourDateSerializer(many=True)

    class Meta:
        model = ConcreteTour
        fields = ('price_KGZ', 'concrete_tour_date')

    def create(self, validated_data):
        concrete_tour_date_data = validated_data.pop('concrete_tour_date')
        concrete_tour = ConcreteTour.objects.create(**validated_data)

        for concrete_tours_date_data in concrete_tour_date_data:
            ConcreteTourDate.objects.create(concrete_tours=concrete_tour, **concrete_tours_date_data)

        return concrete_tour
