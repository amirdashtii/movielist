from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Actor, Director, Writer
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer, WriterSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        quaryset = Movie.objects.all()
        serializer = MovieSerializer(quaryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    movie = get_object_or_404(Actor, pk=id)
    if request.method == 'GET':
        serializer = ActorSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        quaryset = Actor.objects.all()
        serializer = ActorSerializer(quaryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def actor_detail(request, id):
    actor = get_object_or_404(Actor, pk=id)
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorSerializer(actor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def director_list(request):
    if request.method == 'GET':
        quaryset = Director.objects.all()
        serializer = DirectorSerializer(quaryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    director = get_object_or_404(Director, pk=id)
    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(director, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def writer_list(request):
    if request.method == 'GET':
        quaryset = Writer.objects.all()
        serializer = WriterSerializer(quaryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WriterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def writer_detail(request, id):
    writer = get_object_or_404(Writer, pk=id)
    if request.method == 'GET':
        serializer = WriterSerializer(writer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WriterSerializer(writer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        writer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
