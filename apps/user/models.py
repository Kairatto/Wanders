from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class Profile(models.Model):
    GENDER_CHOICES = (
        ('f', 'Женский'),
        ('m', 'Мужской'),
        ('o', 'Другое')
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_profile',
        primary_key=True
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=13, verbose_name='phone')
    avatar = models.ImageField(upload_to='user_avatar')
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    bio = models.CharField(max_length=200, verbose_name='bio')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)
   
    def __str__(self) -> str:
        return self.first_name + self.last_name

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class ProfileImage(models.Model):
    image = models.ImageField(upload_to='profile_images')
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='profile_images'
    )

    class Meta:
        verbose_name = 'Фото пользователя'
        verbose_name_plural = 'Фото пользователей'
