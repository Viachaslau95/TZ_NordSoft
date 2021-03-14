from rest_framework import serializers

from shop.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author')


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Book
        exclude = ('photo',)
