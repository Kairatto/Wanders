from django.db import models

from apps.tour.models import Tour


# class Accommodation(models.Model):
#     description = models.TextField(max_length=999, verbose_name='Общее описание проживания')
#     tour = models.ForeignKey(
#         to=Tour,
#         on_delete=models.CASCADE,
#         related_name='accommodations',
#     )
#
#     class Meta:
#         verbose_name = 'Описание проживания'
#
#
# class AccommodationImages(models.Model):
#     image = models.ImageField(upload_to='accommodation_images')
#     accommodation = models.ForeignKey(
#         to=Accommodation,
#         on_delete=models.CASCADE,
#         related_name='accommodation_images',
#     )
#
# ############ Убрать


class Place(models.Model):
    amount_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
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

    title = models.CharField(max_length=150, verbose_name='Название проживания')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание проживания')
    type_accommodation = models.CharField(max_length=10000, choices=TYPE_ACCOMMODATION_CHOICES, verbose_name='Тип проживания')
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
    image = models.ImageField(upload_to='place_images', blank=False)
    place_residence = models.ForeignKey(
        to=PlaceResidence,
        on_delete=models.CASCADE,
        related_name='place_residence_images',
    )
