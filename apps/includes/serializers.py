from rest_framework import serializers

from .models import NotIncluded, Included


class IncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Included
        fields = ('included', )


class NotIncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotIncluded
        fields = ('not_included', )
