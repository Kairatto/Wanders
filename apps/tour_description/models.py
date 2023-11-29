from django.db import models

from apps.tour.models import Tour


class TourDescription(models.Model):
    description = models.TextField()
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='tour_description',
    )

    class Meta:
        verbose_name = 'Описание тура'
        verbose_name_plural = 'Описание туров'


class DescriptionDetail(models.Model):
    title = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='description_images', blank=True)
    tour_description = models.ForeignKey(
        to=TourDescription,
        on_delete=models.CASCADE,
        related_name='description_details',
    )
