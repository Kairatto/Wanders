from django.db import models

from apps.tour.models import Tour


class Days(models.Model):
    title = models.CharField(max_length=10000, verbose_name='Название дня')
    description = models.TextField(max_length=10000, blank=True,  verbose_name='Описание дня')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='days',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class DaysImage(models.Model):
    image = models.ImageField(upload_to='days_images')
    day = models.ForeignKey(
        to=Days,
        on_delete=models.CASCADE,
        related_name='days_images',
    )
