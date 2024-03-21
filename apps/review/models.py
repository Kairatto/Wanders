from django.db import models
from django.contrib.auth import get_user_model

from apps.tour.models import Tour

User = get_user_model()


class Review(models.Model):

    ABOUT_CHOICES = (
        ('Organizer', 'Об организаторе'),
        ('Guide', 'Об Гиде'),
    )

    comment = models.TextField(max_length=10000, verbose_name='Отзыв')
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка')
    about = models.CharField(max_length=10000, choices=ABOUT_CHOICES, verbose_name='Комментария о ком')

    tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self) -> str:
        return self.comment

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
