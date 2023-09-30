from django.db import models
from slugify import slugify


class Tour(models.Model):
    title_tour = models.CharField(max_length=300, verbose_name='Название тура')
    text_tour = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    slug = models.SlugField(max_length=300, unique=True, blank=True)

    def __str__(self) -> str:
        return self.title_tour

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.title_tour}")
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
