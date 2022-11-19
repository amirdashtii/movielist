from django.contrib import admin
from .models import Movie, Actor, Director, Writer


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    list_editable = ['year']


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
