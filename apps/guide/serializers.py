from rest_framework import serializers

from .models import Guide


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('first_name', 'last_name', 'description', 'photo')
