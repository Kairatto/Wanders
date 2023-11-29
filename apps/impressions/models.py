from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class Impression(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(max_length=999, blank=True,  verbose_name='Описание')
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='impression',
    )

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
            while Impression.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Главное впечатление'
        verbose_name_plural = 'Главные впечатления'


class ImpressionImages(models.Model):
    image = models.ImageField(upload_to='impression_images')
    impression = models.ForeignKey(
        to=Impression,
        on_delete=models.CASCADE,
        related_name='impression_images',
    )
