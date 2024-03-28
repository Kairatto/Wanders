from django.db import models

from apps.tour.models import Tour


class Included(models.Model):
    included = models.CharField(max_length=10000, verbose_name='Включено в стоимость тура', blank=True, null=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='included',
    )

    def __str__(self) -> str:
        return self.included

    class Meta:
        verbose_name = 'Включено в стоимость тура'
        verbose_name_plural = 'Включены в стоимость тура'


class NotIncluded(models.Model):
    not_included = models.CharField(max_length=10000, verbose_name='Не включено в стоимость тура', blank=True, null=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='not_included',
    )

    def __str__(self) -> str:
        return self.not_included

    class Meta:
        verbose_name = 'Не включено в стоимость тура'
        verbose_name_plural = 'Не включены в стоимость тура'
