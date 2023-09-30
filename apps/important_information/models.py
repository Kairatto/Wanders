from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class ImportantInformation(models.Model):
    title_important_information = models.CharField(max_length=300, verbose_name='Важно знать')
    description_important_information = models.TextField(blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='important_informations',
    )

    def __str__(self) -> str:
        return self.title_important_information

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title_important_information}")
            slug = base_slug
            counter = 1
            while Tour.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Важно знать'
