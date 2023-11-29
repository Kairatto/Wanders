from rest_framework import serializers

from .models import CancelReservation


class CancelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancelReservation
        fields = ('slug', 'title', 'description', 'file')
