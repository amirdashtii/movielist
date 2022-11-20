from django_filters.rest_framework import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'actor__id': ['exact'],
            'director__id': ['exact'],
            'writer__id': ['exact'],
            'year': ['gte', 'lte'],
        }
