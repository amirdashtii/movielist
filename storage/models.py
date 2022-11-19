from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    orginal_title = models.CharField(max_length=255, null=True)
    year = models.FloatField(max_length=4, null=True)
    runtime = models.FloatField(max_length=3, null=True)
    genre = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    poster = models.ImageField(null=True)
    imdb_id = models.CharField(max_length=20, unique=True, null=True)


class Actor(models.Model):
    full_name = models.ManyToManyField(Movie, null=True)


class Writer(models.Model):
    full_name = models.ManyToManyField(Movie, null=True)


class Director(models.Model):
    full_name = models.ManyToManyField(Movie, null=True)
