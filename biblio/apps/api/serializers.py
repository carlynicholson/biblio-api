from rest_framework import serializers
from ..api.models import (
    Favorite, Book
)


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author',
                  'genre', 'pages',
                  'published', 'publisher',
                  'description', 'is_favorite',
                  'is_public')


class FavoritesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    books = BookSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Favorite
        fields = ('id', 'owner', 'created_at', 'updated_at')
