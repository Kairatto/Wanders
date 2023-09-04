from rest_framework import serializers
from .models import News, Comment


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    image = serializers.ImageField()


class CommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    image = serializers.ImageField()
    news = NewsSerializer(required=True, allow_null=None)

    def create(self, validated_data):
        news_data = validated_data.pop('news', None)
        news_obj, _ = News.objects.get_or_create(**news_data)
        comment_obj = Comment.objects.create(news=news_obj, **validated_data)
        return comment_obj

