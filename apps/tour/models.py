from django.db import models
from slugify import slugify


class Tour(models.Model):
    title_tour = models.CharField(max_length=200, verbose_name='Название тура')
    text_tour = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)

    def __str__(self) -> str:
        return self.title_tour

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_tour)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
