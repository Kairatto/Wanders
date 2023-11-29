from django.db import models
from slugify import slugify


class Collection(models.Model):
    slug = models.SlugField(primary_key=True, max_length=35, blank=True)
    collection = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.collection)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.collection

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'


class Activity(models.Model):
    slug = models.SlugField(primary_key=True, max_length=35, blank=True)
    activity = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.activity)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.activity

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


class Country(models.Model):
    slug = models.SlugField(primary_key=True, max_length=35, blank=True)
    country = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.country)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class TouristRegion(models.Model):
    slug = models.SlugField(primary_key=True, max_length=35, blank=True)
    region = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.region)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.region

    class Meta:
        verbose_name = 'Туристический регион'
        verbose_name_plural = 'Туристические регионы'


class Location(models.Model):
    slug = models.SlugField(primary_key=True, max_length=35, blank=True)
    location = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.location)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.location

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class City(models.Model):
    slug = models.SlugField(primary_key=True, max_length=35, blank=True)
    city = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
