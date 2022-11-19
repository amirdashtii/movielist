from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    orginal_title = models.CharField(max_length=255)
    year = models.DateField()
    runtime = models.FloatField(max_length=3)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    poster = models.ImageField()
    imdb_id = models.CharField(max_length=20, unique=True)


class Actor(models.Model):
    full_name = models.ManyToManyField(Movie)


class Writer(models.Model):
    full_name = models.ManyToManyField(Movie)


class Director(models.Model):
    full_name = models.ManyToManyField(Movie)
