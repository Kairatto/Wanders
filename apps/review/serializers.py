from rest_framework import serializers

from apps.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'comment', 'rating', 'about', 'tour', 'created')
