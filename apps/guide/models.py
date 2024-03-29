from django.db import models
from slugify import slugify


class Guide(models.Model):
    first_name = models.CharField(max_length=10000, verbose_name='Имя гида', blank=True, null=True)
    last_name = models.CharField(max_length=10000, verbose_name='Фамилия гида', blank=True, null=True)
    description = models.TextField(verbose_name='Описание гида', blank=True, null=True)
    photo = models.ImageField(upload_to='avatar_guide', blank=True, null=True)
    slug = models.SlugField(max_length=10000, unique=True, blank=True)

    def __str__(self) -> str:
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ""
        super().save(*args, **kwargs)

        if not self.slug:
            base_slug = slugify(f"{self.id}-{self.first_name}")
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
