from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        unique_together = ('first_name', 'last_name', 'patronymic')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')

    class Meta:
        unique_together = ('title', 'author', 'pub_year', 'publisher')

    def __str__(self):
        return self.title