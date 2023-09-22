from rest_framework import serializers
from .models import Tour, ImportantInformation


class ImportantInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantInformation
        fields = ('slug', 'title_important_information', 'description_important_information')
