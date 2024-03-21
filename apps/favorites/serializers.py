from rest_framework import serializers

from .models import FeaturedTours
from ..account.serializers import UserSerializer


class FeaturedToursSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = FeaturedTours
        fields = ('id', 'author', 'tour')
