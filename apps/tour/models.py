from django.db import models
from slugify import slugify

from apps.tags.models import Activity, City, Country, Collection, Location, TouristRegion


class Tour(models.Model):

    LANGUAGE_CHOICES = (
        ('Russian', 'Русский'),
        ('English', 'Английский'),
        ('Kyrgyz', 'Кыргызкий'),
    )

    DIFFICULTY_LEVEL_CHOICES = (
        ('Base', 'Базовый'),
        ('Medium', 'Средний'),
        ('Advanced', 'Продвинутый'),
    )

    TOUR_CURRENCY_CHOICES = (
        ('KGS', 'Кыргызский СОМ, "KGS"'),
        ('RUB', 'Российский РУБЛЬ, "RUB"'),
        ('USD', 'Доллар США, "USD"'),
    )

    TYPE_TOUR_CHOICES = (
        ('AUTHORS', 'Авторский'),
        ('GROUP', 'Групповой'),
    )

    COMFORT_LEVEL_CHOICES = (
        ('Base', 'Базовый'),
        ('Simple', 'Простой'),
        ('Medium', 'Средний'),
        ('Above_average', 'Выше среднего'),
        ('High', 'Высокий'),
    )

    INSURANCE_CONDITIONS_CHOICES = (
        ('included', 'Страховка включена в стоимость тура'),
        ('not_included', 'Страховка не включена в стоимость тура'),
        ('required_not_included', 'Страховка обязательна и не включена в стоимость тура'),
    )

    title = models.CharField(max_length=300, verbose_name='Название тура')
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, verbose_name='Языки')

    amount_of_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    min_people = models.PositiveSmallIntegerField(verbose_name='Минимальное количество человек')
    max_people = models.PositiveSmallIntegerField(verbose_name='Максимальное количество человек')
    min_age = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст человека')
    max_age = models.PositiveSmallIntegerField(verbose_name='Максимальный возраст человека')

    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_LEVEL_CHOICES, verbose_name='Уровень сложности')
    comfort_level = models.CharField(max_length=200, choices=COMFORT_LEVEL_CHOICES, verbose_name='Уровень комфорта в туре')
    tour_currency = models.CharField(max_length=50, choices=TOUR_CURRENCY_CHOICES, verbose_name='Валюта тура')
    insurance_conditions = models.CharField(max_length=200, choices=INSURANCE_CONDITIONS_CHOICES, verbose_name='Условия страхования')
    type_tour = models.CharField(max_length=200, choices=TYPE_TOUR_CHOICES, verbose_name='Тип тура')

    included_in_the_price = models.TextField(max_length=5000, blank=True, verbose_name='Включено в стоимость')
    not_included_in_the_price = models.TextField(max_length=5000, blank=True, verbose_name='Не включено в стоимость')
    recommendations = models.TextField(max_length=1000, blank=True, verbose_name='Рекомендации для покупки билетов')
    list_of_things = models.TextField(max_length=1000, blank=True, verbose_name='Cписок вещей')
    address_point = models.TextField(max_length=999, verbose_name='Адрес точки сбора')
    description_point = models.TextField(max_length=999, verbose_name='Комментарий для туриста')

    city = models.ManyToManyField(to=City, related_name='collection_point_city')
    activity = models.ManyToManyField(to=Activity, related_name='tour_activities')
    country = models.ManyToManyField(to=Country, related_name='tour_country')
    collection = models.ManyToManyField(to=Collection, related_name='tour_collection')
    location = models.ManyToManyField(to=Location, related_name='tour_location')
    tourist_region = models.ManyToManyField(to=TouristRegion, related_name='tourist_region')

    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    slug = models.SlugField(max_length=300, unique=True, blank=True)

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


class Question(models.Model):
    question = models.CharField(max_length=1000, verbose_name='Вопрос')
    answer = models.TextField(max_length=2000, verbose_name='Ответ')
    tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE, related_name='question')

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = 'Вопрос ответ'
        verbose_name_plural = 'Вопросы ответы'
