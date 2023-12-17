from django.db import models

from apps.tags.models import TouristRegion
from apps.tour.models import Tour


class CollectionPoint(models.Model):
    address = models.CharField(max_length=300, verbose_name='Адрес точки сбора')
    description = models.TextField(max_length=999, verbose_name='Комментарий для туриста')
    tourist_region = models.ManyToManyField(to=TouristRegion, related_name='collection_point')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='collection_point',
    )

    class Meta:
        verbose_name = 'Точка сбора'
        verbose_name_plural = 'Точки сбора'

