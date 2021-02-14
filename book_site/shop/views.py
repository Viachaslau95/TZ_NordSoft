from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Book, Author
from .forms import BookForm


class HomeBooks(ListView):
    model = Book
    template_name = 'shop/home_books_list.html'
    context_object_name = 'books'


class BooksByAuthor(ListView):
    model = Book
    template_name = 'shop/home_books_list.html'
    context_object_name = 'books'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = Author.objects.get(pk=self.kwargs['author_id'])
        return context

    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs['author_id'])


class CreateBook(CreateView):
    form_class = BookForm
    template_name = 'shop/add_book.html'
    success_url = reverse_lazy('home')






