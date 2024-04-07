from django.db import models

from apps.tour.models import Tour
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum


class ConcreteTourDate(models.Model):
    start_date = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    end_date = models.DateField(verbose_name='Дата завершения', blank=True, null=True)

    price_KGZ = models.PositiveSmallIntegerField(verbose_name='Стоимость тура за одно туриста в сомах', blank=True,
                                                 null=True)

    amount_seat = models.IntegerField(default=0, verbose_name='Количество мест', blank=True, null=True)
    total_seats_count = models.IntegerField(default=0, verbose_name='Общее количество забронированных мест', blank=True,
                                            null=True)

    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='concrete_tour_date',
    )

    class Meta:
        verbose_name = 'Дата поездки'
        verbose_name_plural = 'Даты поездок'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.total_seats_count = self.amount_seat
        super(ConcreteTourDate, self).save(*args, **kwargs)


class BookingTour(models.Model):
    seats_count = models.PositiveSmallIntegerField(verbose_name='Количество туристов')
    name = models.CharField(max_length=25, verbose_name='Имя и Фамилия')
    phone = models.CharField(max_length=13, verbose_name='phone')
    email = models.EmailField(max_length=150, verbose_name='email')
    description = models.TextField(verbose_name='Комментарий', blank=True)
    is_verified = models.BooleanField(default=False)
    concrete_tour_date = models.ForeignKey(ConcreteTourDate, on_delete=models.CASCADE, related_name='booking_tour')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


@receiver(post_save, sender=BookingTour)
@receiver(post_delete, sender=BookingTour)
def update_total_seats_count(sender, instance, **kwargs):
    concrete_tour_date = instance.concrete_tour_date
    if concrete_tour_date:
        total_seats_count = \
        BookingTour.objects.filter(concrete_tour_date=concrete_tour_date, is_verified=True).aggregate(
            total_seats=Sum('seats_count'))['total_seats'] or 0
        concrete_tour_date.total_seats_count = concrete_tour_date.amount_seat - total_seats_count
        concrete_tour_date.save()
