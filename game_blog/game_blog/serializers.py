from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'release_year', 'rating', 'review']
        extra_kwargs = {'title': {'required': False}, 'description': {'required': False}, 'release_year': {'required': False}, 'review': {'required': False}}