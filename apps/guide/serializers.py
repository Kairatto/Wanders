from rest_framework import serializers

from .models import Guide


class GuideCRMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('first_name', 'photo')


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('slug', 'id', 'first_name', 'last_name', 'description', 'photo')

    def validate(self, data):
        if Guide.objects.filter(first_name=data['first_name'], last_name=data['last_name']).exists():
            raise serializers.ValidationError("Гид с таким именем и фамилией уже существует.")
        return data


class GuideBunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('slug', 'id', 'first_name', 'last_name', 'description', 'photo')
