from django.db import models

from apps.tour.models import Tour


class TourImages(models.Model):
    image = models.ImageField(upload_to='tour_images')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='tour_images',
        null=True,
        blank=True,
        default=None
    )
