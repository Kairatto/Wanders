from django.db import models
from slugify import slugify

from apps.guide.models import Guide
from django.contrib.auth import get_user_model
from apps.tags.models import (Country, Collection, Location, TouristRegion, Language, InsuranceConditions,
                              DifficultyLevel, ComfortLevel, TypeTour, TourCurrency)


User = get_user_model()


class Tour(models.Model):

    title = models.CharField(max_length=10000, verbose_name='Название тура', blank=True, null=True)
    description = models.TextField(max_length=3000, verbose_name='Описание тура', blank=True, null=True)

    main_location = models.TextField(max_length=10000, verbose_name='Основная локация', blank=True, null=True)
    main_activity = models.TextField(max_length=10000, verbose_name='Основная активность', blank=True, null=True)

    amount_of_days = models.PositiveSmallIntegerField(verbose_name='Количество дней', blank=True, null=True)
    min_people = models.PositiveSmallIntegerField(verbose_name='Минимальное количество человек', blank=True, null=True)
    max_people = models.PositiveSmallIntegerField(verbose_name='Максимальное количество человек', blank=True, null=True)
    min_age = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст человека', blank=True, null=True)
    max_age = models.PositiveSmallIntegerField(verbose_name='Максимальный возраст человека', blank=True, null=True)

    difficulty_level = models.ForeignKey(to=DifficultyLevel, on_delete=models.DO_NOTHING, blank=True, null=True)
    type_tour = models.ForeignKey(to=TypeTour, on_delete=models.DO_NOTHING, blank=True, null=True)
    comfort_level = models.ForeignKey(to=ComfortLevel, on_delete=models.DO_NOTHING, blank=True, null=True)
    insurance_conditions = models.ForeignKey(to=InsuranceConditions, on_delete=models.DO_NOTHING, blank=True, null=True)

    language = models.ManyToManyField(to=Language, blank=True)
    tour_currency = models.ManyToManyField(to=TourCurrency, blank=True)

    country = models.ManyToManyField(to=Country, blank=True)
    collection = models.ManyToManyField(to=Collection, blank=True)
    location = models.ManyToManyField(to=Location, blank=True)
    tourist_region = models.ManyToManyField(to=TouristRegion, blank=True)

    guide = models.ManyToManyField(to=Guide, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    is_archive = models.BooleanField(default=False, verbose_name='Архив')
    is_draft = models.BooleanField(default=False, verbose_name='Черновик')
    is_active = models.BooleanField(default=False, verbose_name='Сотояние тура')
    is_verified = models.BooleanField(default=False, verbose_name='Потверждение администратором')

    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.title if self.title else "Черновик тура"

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)

        if is_new or not self.slug:
            base_slug = slugify(self.title) if self.title else "Черновик-тура"
            self.slug = f"{self.id}-{base_slug}"
            counter = 1
            original_slug = self.slug
            while Tour.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
            super(Tour, self).save(update_fields=['slug'])

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
