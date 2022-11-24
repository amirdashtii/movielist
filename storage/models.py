from django.core.validators import MinValueValidator
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
    year = models.DecimalField(
        max_digits=4, decimal_places=0, null=True, blank=True)
    runtime = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True)
    imdb_id = models.CharField(
        max_length=20, unique=True, null=True, blank=True)
    actor = models.ManyToManyField(Actor, blank=True)
    writer = models.ManyToManyField(Writer, blank=True)
    director = models.ManyToManyField(Director, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class List(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)


class ListItem(models.Model):
    list = models.ForeignKey(
        List, on_delete=models.PROTECT, related_name='items')
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name='listitems')
    # actor = models.ForeignKey(
    #     Actor, on_delete=models.PROTECT, related_name='listitems')
    # director = models.ForeignKey(
    #     Director, on_delete=models.PROTECT, related_name='listitems')
    # writer = models.ForeignKey(
    #     Writer, on_delete=models.PROTECT, related_name='listitems')
