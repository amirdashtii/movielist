from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    orginal_title = models.CharField(max_length=255)
    directors = models.TextField()
    year = models.DateField()
    runtime = models.FloatField(max_length=3)
    writerr = models.TextField()
    actors = models.TextField()
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    poster = models.ImageField()
    imdb_id = models.CharField(max_length=20, unique=True)

