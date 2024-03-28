from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=3000)
    image = models.ImageField(upload_to='about_us_images')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Картина для "О нас"'
        verbose_name_plural = 'Картины для "О нас"'
