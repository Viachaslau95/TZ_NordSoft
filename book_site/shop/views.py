from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'title': 'Книги'

    }
    return render(request, 'shop/index.html', context=context)



