from django.db import models

from apps.tour.models import Tour


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


class Accommodation(models.Model):
    description = models.TextField(max_length=999, verbose_name='Общее описание проживания')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='accommodations',
    )

    class Meta:
        verbose_name = 'Описание проживания'


class AccommodationImages(models.Model):
    image = models.ImageField(upload_to='accommodation_images')
    accommodation = models.ForeignKey(
        to=Accommodation,
        on_delete=models.CASCADE,
        related_name='accommodation_images',
    )


class Place(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название проживания')
    description = models.TextField(max_length=999, blank=True, verbose_name='Описание проживания')
    amount_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    type_accommodation = models.CharField(max_length=200, choices=TYPE_ACCOMMODATION_CHOICES, verbose_name='Тип проживания')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='place',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Место проживания'
        verbose_name_plural = 'Места проживания'


class PlaceImages(models.Model):
    image = models.ImageField(upload_to='place_images')
    place = models.ForeignKey(
        to=Place,
        on_delete=models.CASCADE,
        related_name='place_images',
    )


class AnotherPlace(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название проживания')
    description = models.TextField(max_length=999, blank=True, verbose_name='Описание проживания')
    amount_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    type_accommodation = models.CharField(max_length=200, choices=TYPE_ACCOMMODATION_CHOICES, verbose_name='Тип проживания')
    place = models.ForeignKey(
        to=Place,
        on_delete=models.CASCADE,
        related_name='another_place',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Другой вариант проживания'
        verbose_name_plural = 'Другие варианты проживания'


class AnotherPlaceImages(models.Model):
    image = models.ImageField(upload_to='place_images')
    another_place = models.ForeignKey(
        to=AnotherPlace,
        on_delete=models.CASCADE,
        related_name='another_place_images',
    )
