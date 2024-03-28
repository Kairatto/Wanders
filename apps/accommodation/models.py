from django.db import models

from apps.tour.models import Tour


class Place(models.Model):
    amount_days = models.PositiveSmallIntegerField(verbose_name='Количество дней', blank=True, null=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='place',
    )

    class Meta:
        verbose_name = 'Место проживания'
        verbose_name_plural = 'Места проживания'


class PlaceResidence(models.Model):

    TYPE_ACCOMMODATION_CHOICES = (
        ('Tent', 'Палатка'),
        ('Glamping', 'Глэмпинг'),
        ('Hostel', 'Гостинница'),
        ('Hotel', 'Отель'),
        ('Holiday House', 'Дом отдыха'),
        ('Apartments', 'Апартаменты'),
        ('Camp site', 'Турбаза'),
        ('Sanatorium', 'Санаторий'),
        ('Villa', 'Вилла'),
    )

    title = models.CharField(max_length=150, verbose_name='Название проживания', blank=True, null=True)
    description = models.TextField(max_length=1000, verbose_name='Описание проживания', blank=True, null=True)
    type_accommodation = models.CharField(max_length=10000, choices=TYPE_ACCOMMODATION_CHOICES, verbose_name='Тип проживания', blank=True, null=True)
    place = models.ForeignKey(
        to=Place,
        on_delete=models.CASCADE,
        related_name='place_residence',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Проживания'
        verbose_name_plural = 'Проживания'


class PlaceResidenceImages(models.Model):
    image = models.ImageField(upload_to='place_images', blank=True, null=True)
    place_residence = models.ForeignKey(
        to=PlaceResidence,
        on_delete=models.CASCADE,
        related_name='place_residence_images',
    )
