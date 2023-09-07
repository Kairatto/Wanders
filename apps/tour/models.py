from django.db import models
from slugify import slugify


# class Tour(models.Model):
#     title = models.CharField(max_length=100, verbose_name='Название тура')


class Days(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название дня')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    # tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE, related_name='tour')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class DaysImage(models.Model):
    image = models.ImageField(upload_to='media/day_images')
    day = models.ForeignKey(
        to=Days,
        on_delete=models.CASCADE,
        related_name='day_images',
    )

