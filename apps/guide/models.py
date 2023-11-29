from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class Guide(models.Model):
    first_name = models.CharField(max_length=300, verbose_name='Имя гида')
    last_name = models.CharField(max_length=300, verbose_name='Фамилия гида')
    description = models.TextField(blank=True, verbose_name='Описание гида')
    photo = models.ImageField(upload_to='avatar_guide', blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='guide',
    )

    def __str__(self) -> str:
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.first_name}-{self.last_name}")
            slug = base_slug
            counter = 1
            while Guide.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'
