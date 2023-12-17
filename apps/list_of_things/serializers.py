from rest_framework import serializers

from .models import ListOfThings


class ListOfThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfThings
        fields = ('title', )
