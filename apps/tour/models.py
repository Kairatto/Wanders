from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="news_images/")


class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="comment_images/")
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True)
