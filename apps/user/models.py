from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class Profile(models.Model):
    GENDER_CHOICES = (
        ('female', 'Женский'),
        ('male', 'Мужской'),
        ('other', 'Другое')
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_profile',
        primary_key=True
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name='phone', blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=200, verbose_name='bio', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class ProfileImage(models.Model):
    image = models.ImageField(upload_to='profile_images', blank=True)
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='profile_images'
    )

    class Meta:
        verbose_name = 'Фото пользователя'
        verbose_name_plural = 'Фото пользователей'
