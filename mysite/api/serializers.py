from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'patronymic', 'bio']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pub_year', 'genre', 'category', 'publisher', 'image', 'file']

    def validate(self, attrs):
        title = attrs.get('title')
        author = attrs.get('author')
        pub_year = attrs.get('pub_year')
        publisher = attrs.get('publisher')
        category = attrs.get('category')

        if category.lower() == 'учебник':
            existing = Book.objects.filter(
                title=title,
                author=author,
                category__iexact='учебник',
                pub_year=pub_year,
                publisher=publisher
            ).exists()
            if existing:
                raise serializers.ValidationError(
                    'Такой учебник уже существует (по издательству и году).'
                )

        return attrs