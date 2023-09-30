from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class Accommodation(models.Model):
    COMFORT_CHOICES = (
        ('Base', 'Базовый'),
        ('Simple', 'Простой'),
        ('Medium', 'Средний'),
        ('luxury', 'Люкс'),
        ('Premium', 'Премиум')
    )

    TYPE_CHOICES = (
        ('Tent', 'Палатка'),
        ('Hostel', 'Гостиница'),
        ('Hotel', 'Отель'),
        ('Cottage', 'Котедж')
    )

    title_accommodation = models.CharField(max_length=300, verbose_name='Проживание')
    description_accommodation = models.TextField(blank=True)
    comfort = models.CharField(max_length=13, choices=COMFORT_CHOICES, verbose_name='Степень комфорта')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, verbose_name='Тип проживания')
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='accommodations',
    )

    def __str__(self) -> str:
        return self.title_accommodation

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title_accommodation}")
            slug = base_slug
            counter = 1
            while Tour.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Проживание'


class Hotel(models.Model):
    title_hotel = models.CharField(max_length=300, verbose_name='Название отеля')
    description_hotel = models.TextField(blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    accommodation = models.ForeignKey(
        to=Accommodation,
        on_delete=models.CASCADE,
        related_name='hotels',
    )

    def __str__(self) -> str:
        return self.title_hotel

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title_hotel}")
            slug = base_slug
            counter = 1
            while Tour.objects.filter(slug=slug).exists():
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
        null=True,
        blank=True,
        default=None
    )
