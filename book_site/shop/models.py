from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y,%m/%d/', verbose_name='Фото', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, verbose_name='Автор')
    bought_books = models.IntegerField(default=0, verbose_name='Купленно книг')

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'id': self.pk})

    def __str__(self):
        return f'{self.name} {self.bought_books}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-id']


class Author(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя')

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']
