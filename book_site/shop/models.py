from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y,%m/%d/', verbose_name='Фото', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    number = models.PositiveIntegerField(verbose_name='остаток')  # Это поле для хранения остатков данного продукта.
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'id': self.pk})

    def __str__(self):
        return self.name

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
