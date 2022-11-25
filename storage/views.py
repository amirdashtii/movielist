from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .filters import MovieFilter
from .models import Movie, Actor, Director, Writer, List
from .pagination import DefaultPagination
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer, WriterSerializer, ListSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'actor__full_name',
                     'director__full_name', 'writer__full_name']
    ordering_fields = ['title', 'actor__full_name',
                       'director__full_name', 'writer__full_name']


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer


class ListViewSet(ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return List.objects.all()
        return List.objects.filter(user_id=user.id)
