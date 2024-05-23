"""
Serializers for recipe APIs
"""

from rest_framework import serializers
from core.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title','director','main_character','duration',
        'rating','description']
        read_only_fields = ['title']

class MovieDetailSerializer(MovieSerializer):
    """Serializer for recipe detail view"""

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['description']