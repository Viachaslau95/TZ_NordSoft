from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, FormView, DeleteView, DetailView, TemplateView

from shop.models import Book
from cart.cart import Cart
from cart.forms import CartAddBookForm


class CardAdd(FormView):
    form_class = CartAddBookForm
    success_url = reverse_lazy('cart:cart_detail')
    template_name = 'cart/detail.html'

    def form_valid(self, form, *args, **kwargs):
        cart = Cart(self.request)
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        if form.is_valid():
            cart.add(book=book)
        return super(CardAdd, self).form_valid(form)


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddBookForm(initial={'quantity': item['quantity'],
                                                                'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
