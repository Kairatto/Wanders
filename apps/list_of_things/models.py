from django.db import models

from apps.tour.models import Tour


class ListOfThings(models.Model):
    title = models.CharField(max_length=300, verbose_name='Cписок вещей')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='list_of_things',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Cписок вещей'
        verbose_name_plural = 'Cписки вещей'
