from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class Days(models.Model):
    title_days = models.CharField(max_length=300, verbose_name='Название дня')
    description_days = models.TextField(blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='days',
    )

    def __str__(self) -> str:
        return self.title_days

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title_days}")
            slug = base_slug
            counter = 1
            while Tour.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

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
