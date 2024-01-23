from django.db import models

from apps.tour.models import Tour


class ConcreteTour(models.Model):
    price_KGZ = models.PositiveSmallIntegerField(verbose_name='Стоимость тура за одно туриста в сомах')

    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='concrete_tour',
    )

    class Meta:
        verbose_name = 'Групповая дата'
        verbose_name_plural = 'Групповые даты'


class ConcreteTourDate(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата завершения')

    amount_seat = models.IntegerField(default=0, verbose_name='Количество мест')

    concrete_tour = models.ForeignKey(
        to=ConcreteTour,
        on_delete=models.CASCADE,
        related_name='concrete_tour_date',
    )

    class Meta:
        verbose_name = 'Дата поездки'
        verbose_name_plural = 'Даты поездок'
