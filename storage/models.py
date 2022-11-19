from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name


class Writer(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name


class Director(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    orginal_title = models.CharField(max_length=255, null=True)
    year = models.DecimalField(max_digits=4,decimal_places=0, null=True)
    runtime = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    genre = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    poster = models.ImageField(null=True)
    imdb_id = models.CharField(max_length=20, unique=True, null=True)
    actor = models.ManyToManyField(Actor)
    writer = models.ManyToManyField(Writer)
    director = models.ManyToManyField(Director)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
