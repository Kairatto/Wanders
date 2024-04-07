from rest_framework import serializers
from apps.account.serializers import UserSerializer

from apps.review.models import Review
from apps.tour.utils import get_user_info


class ReviewSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    user_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'comment', 'rating', 'about', 'tour', 'author', 'user_info', 'created')

    def get_user_info(self, obj):
        return get_user_info(obj.author)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        choice_fields = {'about': dict(Review.ABOUT_CHOICES)}
        for field, choices in choice_fields.items():
            value = representation.get(field)
            if value is not None:
                representation[field] = choices.get(value)

        return representation
