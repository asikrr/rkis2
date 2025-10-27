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
        category = attrs.get('category')
        if category is None and self.instance:
            category = self.instance.category

        title = attrs.get('title')
        author = attrs.get('author')
        pub_year = attrs.get('pub_year')
        publisher = attrs.get('publisher')


        if category.lower() == 'учебник':
            existing = Book.objects.filter(
                title=title or self.instance.title,
                author=author or self.instance.author,
                category__iexact='учебник',
                pub_year=pub_year or self.instance.pub_year,
                publisher=publisher or self.instance.publisher
            ).exclude(pk=self.instance.pk if self.instance else None)

            if existing.exists():
                raise serializers.ValidationError(
                    'Такой учебник уже существует (по издательству и году).'
                )

        return attrs