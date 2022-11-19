from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer


@api_view()
def movie_list(request):
    quaryset = Movie.objects.all()
    serializer = MovieSerializer(quaryset, many=True)
    return Response(serializer.data)


@api_view()
def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
