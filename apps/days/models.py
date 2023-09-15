from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class Days(models.Model):
    title_days = models.CharField(max_length=100, verbose_name='Название дня')
    description_days = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='days',
    )

    def __str__(self) -> str:
        return self.title_days

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_days)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class DaysImage(models.Model):
    image = models.ImageField(upload_to='days_images')
    day = models.ForeignKey(
        to=Days,
        on_delete=models.CASCADE,
        related_name='days_images',
        null=True,
        blank=True,
        default=None
    )
