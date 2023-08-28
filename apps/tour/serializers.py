from rest_framework import serializers

from .models import Tour, Information


class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    information = InformationSerializer(many=True)

    class Meta:
        model = Tour
        fields = '__all__'

    def create(self, validated_data):
        information_data = validated_data.pop('information')
        tour = Tour.objects.create(**validated_data)

        for info_data in information_data:
            Information.objects.create(tour=tour, **info_data)

        return tour
