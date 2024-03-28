from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class TourAgent(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='comp_title', unique=True)
    desc = models.CharField(max_length=200, verbose_name='description')
    image = models.ImageField(upload_to='business_images')
    phone = models.CharField(max_length=13, verbose_name='phone')
    email = models.EmailField(max_length=150, verbose_name='email', blank=True)
    additional_contacts = models.TextField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, verbose_name='instagram', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
   
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Тур. агент'
        verbose_name_plural = 'Тур. агенты'
