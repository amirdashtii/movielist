from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import Movie, Actor, Director, Writer


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    autocomplete_fields = ['actor','director','writer']
    list_display = ['title', 'year']
    list_editable = ['year']
    list_per_page: 10
    ordering = ['title', 'year']
    search_fields = ['title__istartswith', 'year__istartswith']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'movie_count']
    list_per_page: 10
    ordering = ['full_name']
    search_fields = ['full_name__istartswith']

    @admin.display(ordering='movie_count')
    def movie_count(self, actor):
        url = (
            reverse('admin:storage_movie_changelist')
            + '?'
            + urlencode({
                "actor__id": str(actor.id)
            }))
        return format_html('<a href="{}"//">{}</a>', url, actor.movie_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            movie_count=Count('movie')
        )


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'movie_count']
    list_per_page: 10
    ordering = ['full_name']
    search_fields = ['full_name__istartswith']

    @admin.display(ordering='movie_count')
    def movie_count(self, director):
        url = (
            reverse('admin:storage_movie_changelist')
            + '?'
            + urlencode({
                "director__id": str(director.id)
            }))
        return format_html('<a href="{}"//">{}</a>', url, director.movie_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            movie_count=Count('movie')
        )


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'movie_count']
    list_per_page: 10
    ordering = ['full_name']
    search_fields = ['full_name__istartswith']

    @admin.display(ordering='movie_count')
    def movie_count(self, writer):
        url = (
            reverse('admin:storage_movie_changelist')
            + '?'
            + urlencode({
                "writer__id": str(writer.id)
            }))
        return format_html('<a href="{}"//">{}</a>', url, writer.movie_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            movie_count=Count('movie')
        )
