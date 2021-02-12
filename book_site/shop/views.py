from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'title': 'Книги',
        'authors': authors,
    }
    return render(request, 'shop/index.html', context=context)


def get_author(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    authors = Author.objects.all()
    author = Author.objects.get(pk=author_id)
    return render(request, 'shop/author.html', {'books':books, 'authors': authors, 'author': author})






