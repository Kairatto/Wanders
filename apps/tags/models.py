from django.db import models
from slugify import slugify


class Collection(models.Model):
    collection = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.collection

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'


class Activity(models.Model):
    activity = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.activity

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'


class Country(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class TouristRegion(models.Model):
    region = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.region

    class Meta:
        verbose_name = 'Туристический регион'
        verbose_name_plural = 'Туристические регионы'


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.location

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class City(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
