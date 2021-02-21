from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.forms import CartAddBookForm


from .models import Book, Author
from .forms import BookForm


class HomeBooks(ListView):
    model = Book
    template_name = 'shop/home_books_list.html'
    context_object_name = 'books'
    paginate_by = 20


class BooksByAuthor(ListView):
    model = Book
    template_name = 'shop/home_books_list.html'
    context_object_name = 'books'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = Author.objects.get(pk=self.kwargs['author_id'])
        return context

    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs['author_id'])


class CreateBook(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = 'shop/add_book.html'
    success_url = reverse_lazy('home')
    # login_url = '/admin/'
    raise_exception = True


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book_detail.html', {'book': book,
                                                     'cart_book_form': cart_book_form})



