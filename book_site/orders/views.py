from django.shortcuts import render
from django.views.generic import CreateView

from orders.models import OrderItem, Order
from orders.forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/create.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        if self.request.method == 'POST':
            form = OrderCreateForm(self.request.POST)
            order = form.save()
            if form.is_valid():
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        book=item['book'],
                        price=item['price'],
                        quantity=item['quantity']
                        )
            # очистка корзины
            cart.clear()
            return render(self.request, 'orders/created.html',
                          {'order': order})
        else:
            form = OrderCreateForm

        return render(self.request, 'orders/create.html',
                      {'cart': cart, 'form': form})


