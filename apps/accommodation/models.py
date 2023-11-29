from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class Accommodation(models.Model):
    description = models.TextField(max_length=999, verbose_name='Общее описание проживания')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='accommodations',
    )

    class Meta:
        verbose_name = 'Проживание'


class AccommodationImages(models.Model):
    image = models.ImageField(upload_to='accommodation_images')
    accommodation = models.ForeignKey(
        to=Accommodation,
        on_delete=models.CASCADE,
        related_name='accommodation_images',
    )


class Hotel(models.Model):
    title = models.CharField(max_length=300, verbose_name='Место проживания')
    description = models.TextField(max_length=999, blank=True, verbose_name='Описание проживания')
    amount_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    #  ПОМЕСТИТЬ СЮДА МОДЕЛЬ ТИП ПРОЖИВАНИЯ
    #  ОТМЕНА БРОНИРОВАНИЯ ЭТО МОДЕЛЬ
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    accommodation = models.ForeignKey(
        to=Accommodation,
        on_delete=models.CASCADE,
        related_name='hotels',
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title}")
            slug = base_slug
            counter = 1
            while Hotel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class HotelImages(models.Model):
    image = models.ImageField(upload_to='hotel_images')
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE,
        related_name='hotel_images',
    )


class AnotherHotel(models.Model):
    title = models.CharField(max_length=300, verbose_name='Место проживания')
    description = models.TextField(max_length=999, blank=True, verbose_name='Описание проживания')
    amount_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE,
        related_name='another_hotels',
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title}")
            slug = base_slug
            counter = 1
            while Hotel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Другой вариант проживания'
        verbose_name_plural = 'Другие варианты проживания'


class AnotherHotelImages(models.Model):
    image = models.ImageField(upload_to='hotel_images')
    another_hotel = models.ForeignKey(
        to=AnotherHotel,
        on_delete=models.CASCADE,
        related_name='another_hotel_images',
    )
