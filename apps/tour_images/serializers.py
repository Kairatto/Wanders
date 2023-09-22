from rest_framework import serializers
from .models import TourImages


class TourImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImages
        fields = ('image',)
