from django.db import models
from slugify import slugify


class Collection(models.Model):
    collection = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.collection

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.collection}")
            slug = base_slug
            counter = 1
            while Collection.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'


# class Activity(models.Model):
#     activity = models.CharField(max_length=10000)
#     slug = models.SlugField(max_length=10000, unique=True, blank=True)
#
#     def __str__(self) -> str:
#         return self.activity
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = ""
#         super().save(*args, **kwargs)
#
#         if not self.slug:
#             base_slug = slugify(f"{self.id}-{self.activity}")
#             slug = base_slug
#             counter = 1
#             while Activity.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#             self.slug = slug
#             self.save()
#
#     class Meta:
#         verbose_name = 'Активность'
#         verbose_name_plural = 'Активности'


class Country(models.Model):
    country = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.country

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.country}")
            slug = base_slug
            counter = 1
            while Country.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class TouristRegion(models.Model):
    region = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.region

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.region}")
            slug = base_slug
            counter = 1
            while TouristRegion.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Туристический регион'
        verbose_name_plural = 'Туристические регионы'


class Location(models.Model):
    location = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.location

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.location}")
            slug = base_slug
            counter = 1
            while Location.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class MainLocation(models.Model):
    main_location = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.main_location

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.main_location}")
            slug = base_slug
            counter = 1
            while MainLocation.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Основная локация'
        verbose_name_plural = 'Основная локации'
