from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class ImportantInformation(models.Model):
    title_important_information = models.CharField(max_length=300, verbose_name='Важно знать')
    description_important_information = models.TextField(blank=True)
    slug = models.SlugField(max_length=300, primary_key=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='important_informations',
    )

    def __str__(self) -> str:
        return self.title_important_information

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_important_information)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Важно знать'
