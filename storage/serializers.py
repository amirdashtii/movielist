from rest_framework import serializers
from .models import Movie, Actor, Director, Writer, List, ListItem


class MovieSerializer(serializers.ModelSerializer):
    actor = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='full_name'
    )
    writer = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='full_name'
    )
    director = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='full_name'
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'actor', 'director', 'writer']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor()
        fields = ['id', 'full_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director()
        fields = ['id', 'full_name']


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer()
        fields = ['id', 'full_name']


class ListItemSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = ListItem
        fields = ['id', 'movie']


class ListSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ['user', 'id', 'name', 'description', 'items']
