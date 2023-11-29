from django.db import models
from slugify import slugify

from apps.tour.models import Tour


class CancelReservation(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок отмены бронирования')
    description = models.TextField(max_length=999, verbose_name='Описание отмены бронирования')
    file = models.FileField(upload_to="cancel_reservation_file", blank=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='cancel_reservation',
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
            while CancelReservation.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            self.save()

    class Meta:
        verbose_name = 'Условие отмены бронирования'
        verbose_name_plural = 'Условии отмены бронирования'
