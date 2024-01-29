from django.db import models

from apps.tour.models import Tour


class Recommendations(models.Model):
    title = models.CharField(max_length=10000, verbose_name='Рекомендация для покупки билетов')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='recommendations',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Рекомендация для покупки билетов'
        verbose_name_plural = 'Рекомендации для покупки билетов'
