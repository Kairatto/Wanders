from django.db import models


class Information(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class Tour(models.Model):
    title = models.CharField(max_length=200)
    information = models.ManyToManyField(Information, blank=True)
    image = models.ImageField(upload_to="tour_images/")

    def __str__(self):
        return self.title
