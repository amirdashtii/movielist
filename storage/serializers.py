from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    year = serializers.DecimalField(max_digits=4, decimal_places=0)