from django.db import models

from apps.tour.models import Tour


class Guide(models.Model):
    first_name = models.CharField(max_length=10000, verbose_name='Имя гида')
    last_name = models.CharField(max_length=10000, verbose_name='Фамилия гида')
    description = models.TextField(blank=True, verbose_name='Описание гида')
    photo = models.ImageField(upload_to='avatar_guide', blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='guide',
    )

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'
