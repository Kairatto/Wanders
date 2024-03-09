from django.db import models
from slugify import slugify


class InsuranceConditions(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while InsuranceConditions.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Условие страхования'
        verbose_name_plural = 'Условия страхования'


class ComfortLevel(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while ComfortLevel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Уровень комфорта в туре'
        verbose_name_plural = 'Уровни комфорта в турах'


class TypeTour(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while TypeTour.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы туров'


class TourCurrency(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while TourCurrency.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Валюта тура'
        verbose_name_plural = 'Валюта туров'


class DifficultyLevel(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while DifficultyLevel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Уровень сложности'
        verbose_name_plural = 'Уровни сложности'


class Language(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while Language.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Collection(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while Collection.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'


class Country(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while Country.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class TouristRegion(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
            while TouristRegion.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Туристический регион'
        verbose_name_plural = 'Туристические регионы'


class Location(models.Model):
    title = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

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
