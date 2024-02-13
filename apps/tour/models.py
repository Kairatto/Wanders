from django.db import models
from slugify import slugify

from apps.tags.models import MainLocation, Country, Collection, Location, TouristRegion


class Tour(models.Model):

    LANGUAGE_CHOICES = (
        ('Russian', 'Русский'),
        ('English', 'Английский'),
        ('Kyrgyz', 'Кыргызкий'),
    )

    DIFFICULTY_LEVEL_CHOICES = (
        ('Beginner', 'Легкий'),
        ('Moderate', 'Средний'),
        ('Advanced', 'Продвинутый'),
    )

    TOUR_CURRENCY_CHOICES = (
        ('KGS', 'Кыргызский СОМ'),
        ('RUB', 'Российский РУБЛЬ'),
        ('USD', 'Доллар США'),
    )

    TYPE_TOUR_CHOICES = (
        ('AUTHORS', 'Авторский'),
        ('GROUP', 'Групповой'),
    )

    COMFORT_LEVEL_CHOICES = (
        ('Base', 'Базовый'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
    )

    INSURANCE_CONDITIONS_CHOICES = (
        ('included', 'Страховка включена в стоимость тура'),
        ('not_included', 'Страховка не включена в стоимость тура'),
        ('required_not_included', 'Страховка обязательна и не включена в стоимость тура'),
    )

    title = models.CharField(max_length=10000, verbose_name='Название тура')
    description = models.TextField(max_length=10000, verbose_name='Описание тура')

    cancel_reservation = models.TextField(max_length=10000, verbose_name='Условия отмены бронирования')

    amount_of_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    min_people = models.PositiveSmallIntegerField(verbose_name='Минимальное количество человек')
    max_people = models.PositiveSmallIntegerField(verbose_name='Максимальное количество человек')
    min_age = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст человека')
    max_age = models.PositiveSmallIntegerField(verbose_name='Максимальный возраст человека')

    language = models.CharField(max_length=10000, choices=LANGUAGE_CHOICES, verbose_name='Языки')
    difficulty_level = models.CharField(max_length=10000, choices=DIFFICULTY_LEVEL_CHOICES, verbose_name='Уровень сложности')
    tour_currency = models.CharField(max_length=10000, choices=TOUR_CURRENCY_CHOICES, verbose_name='Валюта тура', blank=True)
    type_tour = models.CharField(max_length=10000, choices=TYPE_TOUR_CHOICES, verbose_name='Тип тура')
    comfort_level = models.CharField(max_length=10000, choices=COMFORT_LEVEL_CHOICES, verbose_name='Уровень комфорта в туре')
    insurance_conditions = models.CharField(max_length=10000, choices=INSURANCE_CONDITIONS_CHOICES, verbose_name='Условия страхования')

    main_location = models.ManyToManyField(to=MainLocation, )
    # activity = models.ManyToManyField(to=Activity, )
    country = models.ManyToManyField(to=Country, )
    collection = models.ManyToManyField(to=Collection, )
    location = models.ManyToManyField(to=Location, )
    tourist_region = models.ManyToManyField(to=TouristRegion, )

    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
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
            while Tour.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
