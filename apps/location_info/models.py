from django.db import models
from slugify import slugify

from apps.tour.models import Tour
from apps.tags.models import Activity, MainLocation, Country, Collection, Location, TouristRegion


class LocationInfo(models.Model):
    title = models.CharField(max_length=10000, verbose_name='Информация локации')
    short_description = models.TextField(max_length=10000, blank=True,  verbose_name='Краткое описнаие локации')
    description = models.TextField(max_length=10000, blank=True,  verbose_name='Описнаие локации')
    how_to_get_there = models.TextField(max_length=10000, blank=True,  verbose_name='Как добраться?')
    coordinates = models.CharField(max_length=10000, verbose_name='Координаты')
    coordinates_map = models.CharField(max_length=10000, verbose_name='Координаты на карте')

    main_location = models.ManyToManyField(to=MainLocation, )
    activity = models.ManyToManyField(to=Activity,)
    country = models.ManyToManyField(to=Country, )
    collection = models.ManyToManyField(to=Collection,)
    location = models.ManyToManyField(to=Location, )
    tourist_region = models.ManyToManyField(to=TouristRegion, )
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
        verbose_name = 'Страница локации'
        verbose_name_plural = 'Страница локаций'


class LocationInfoImage(models.Model):
    image = models.ImageField(upload_to='location_info_images')
    location_info = models.ForeignKey(
        to=LocationInfo,
        on_delete=models.CASCADE,
        related_name='location_info_images',
    )


class GettingThere(models.Model):
    title = models.CharField(max_length=10000, verbose_name='Название варианта')
    travel_time = models.CharField(max_length=10000, verbose_name='Время в пути')
    price_travel = models.CharField(max_length=10000, verbose_name='Стоимость проезда')
    description = models.TextField(max_length=10000, blank=True,  verbose_name='Описание')

    location_info = models.ForeignKey(
        to=LocationInfo,
        on_delete=models.CASCADE,
        related_name='getting_there',
    )
