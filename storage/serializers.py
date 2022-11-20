
from rest_framework import serializers
from storage.models import Movie, Actor, Director, Writer


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
        model = Actor()
        fields = ['id', 'full_name']
