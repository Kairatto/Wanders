from django.db import models

from apps.tour.models import Tour


class ConcreteTour(models.Model):
    price_KGZ = models.PositiveSmallIntegerField(verbose_name='Стоимость тура за одно туриста в сомах')
    price_RUB = models.PositiveSmallIntegerField(verbose_name='Стоимость тура за одно туриста в рублях')
    price_USD = models.PositiveSmallIntegerField(verbose_name='Стоимость тура за одно туриста в долларах')

    prepayment_period = models.PositiveSmallIntegerField(verbose_name='За сколько дней до начала тура внести предоплату')
    prepayment_amount = models.PositiveSmallIntegerField(verbose_name='Размер предоплаты в %')

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
