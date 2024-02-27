from django.db import models
from slugify import slugify


class InsuranceConditions(models.Model):
    insurance_conditions = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.insurance_conditions

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.insurance_conditions}")
            slug = base_slug
            counter = 1
            while InsuranceConditions.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Условие страхования'
        verbose_name_plural = 'Условия страхования'


class ComfortLevel(models.Model):
    comfort_level = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.comfort_level

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.comfort_level}")
            slug = base_slug
            counter = 1
            while ComfortLevel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Уровень комфорта в туре'
        verbose_name_plural = 'Уровни комфорта в турах'


class TypeTour(models.Model):
    type_tour = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.type_tour

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.type_tour}")
            slug = base_slug
            counter = 1
            while TypeTour.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы туров'


class TourCurrency(models.Model):
    tour_currency = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.tour_currency

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.tour_currency}")
            slug = base_slug
            counter = 1
            while TourCurrency.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Валюта тура'
        verbose_name_plural = 'Валюта туров'


class DifficultyLevel(models.Model):
    difficulty_level = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.difficulty_level

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.difficulty_level}")
            slug = base_slug
            counter = 1
            while DifficultyLevel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Уровень сложности'
        verbose_name_plural = 'Уровни сложности'


class Language(models.Model):
    language = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.language

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.language}")
            slug = base_slug
            counter = 1
            while Language.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


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


# class MainLocation(models.Model):
#     main_location = models.CharField(max_length=10000)
#     slug = models.SlugField(max_length=10000, unique=True, blank=True)
#
#     def __str__(self) -> str:
#         return self.main_location
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = ""
#         super().save(*args, **kwargs)
#
#         if not self.slug:
#             base_slug = slugify(f"{self.id}-{self.main_location}")
#             slug = base_slug
#             counter = 1
#             while MainLocation.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#             self.slug = slug
#             self.save()
#
#     class Meta:
#         verbose_name = 'Основная локация'
#         verbose_name_plural = 'Основная локации'


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
