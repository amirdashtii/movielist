from django.conf import settings
from django.db import models


class Actor(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        ordering = ['full_name']


class Writer(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        ordering = ['full_name']


class Director(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        ordering = ['full_name']


class Movie(models.Model):
    title = models.CharField(max_length=255)
    orginal_title = models.CharField(max_length=255, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    rated = models.CharField(max_length=255, null=True, blank=True)
    released = models.CharField(max_length=255, null=True, blank=True)
    runtime = models.PositiveIntegerField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    director = models.ManyToManyField(Director, blank=True)
    writer = models.ManyToManyField(Writer, blank=True)
    actor = models.ManyToManyField(Actor, blank=True)
    plot = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    awards = models.TextField(null=True, blank=True)
    poster = models.URLField(max_length=200, null=True, blank=True)
    ratings = models.TextField(null=True, blank=True)
    metascore = models.PositiveIntegerField(null=True, blank=True)
    imdbRating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True)
    imdb_id = models.CharField(
        max_length=20, unique=True, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class List(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class ListItem(models.Model):
    list = models.ForeignKey(
        List, on_delete=models.PROTECT, related_name='items')
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name='listitems')
