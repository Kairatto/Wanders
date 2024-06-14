from django.db import models

from apps.tour.models import Tour


class Days(models.Model):
    title = models.CharField(max_length=3000, verbose_name='Название дня', blank=True, null=True)
    description = models.TextField(max_length=1000, verbose_name='Описание дня', blank=True, null=True)
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
    image = models.ImageField(upload_to='days_images', blank=True, null=True)
    day = models.ForeignKey(
        to=Days,
        on_delete=models.CASCADE,
        related_name='days_images',
    )
