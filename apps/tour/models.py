from django.db import models
from slugify import slugify

from apps.guide.models import Guide
from apps.tags.models import (Country, Collection, Location, TouristRegion, Language, InsuranceConditions,
                              DifficultyLevel, ComfortLevel, TypeTour, TourCurrency)


class Tour(models.Model):

    title = models.CharField(max_length=10000, verbose_name='Название тура')
    description = models.TextField(max_length=3000, verbose_name='Описание тура')

    main_location = models.TextField(max_length=10000, verbose_name='Основная локация')
    main_activity = models.TextField(max_length=10000, verbose_name='Основная активность')

    amount_of_days = models.PositiveSmallIntegerField(verbose_name='Количество дней')
    min_people = models.PositiveSmallIntegerField(verbose_name='Минимальное количество человек')
    max_people = models.PositiveSmallIntegerField(verbose_name='Максимальное количество человек')
    min_age = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст человека')
    max_age = models.PositiveSmallIntegerField(verbose_name='Максимальный возраст человека')

    difficulty_level = models.ForeignKey(to=DifficultyLevel, on_delete=models.DO_NOTHING)
    type_tour = models.ForeignKey(to=TypeTour, on_delete=models.DO_NOTHING)
    comfort_level = models.ForeignKey(to=ComfortLevel, on_delete=models.DO_NOTHING)
    insurance_conditions = models.ForeignKey(to=InsuranceConditions, on_delete=models.DO_NOTHING)

    language = models.ManyToManyField(to=Language, )
    tour_currency = models.ManyToManyField(to=TourCurrency, )

    country = models.ManyToManyField(to=Country, )
    collection = models.ManyToManyField(to=Collection, )
    location = models.ManyToManyField(to=Location, )
    tourist_region = models.ManyToManyField(to=TouristRegion, )

    guide = models.ManyToManyField(to=Guide, )

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
