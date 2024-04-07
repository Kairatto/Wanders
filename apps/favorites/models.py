from django.db import models
from django.contrib.auth import get_user_model

from apps.tour.models import Tour


User = get_user_model()


class FeaturedTours(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранный тур'
        verbose_name_plural = 'Избранные туры'
