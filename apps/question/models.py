from django.db import models

from apps.tour.models import Tour


class Question(models.Model):
    question = models.CharField(max_length=1000, verbose_name='Вопрос')
    answer = models.TextField(max_length=3000, verbose_name='Ответ')
    tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE, related_name='question')

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = 'Вопрос ответ'
        verbose_name_plural = 'Вопросы ответы'
