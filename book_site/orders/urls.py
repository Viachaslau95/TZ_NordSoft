from django.conf.urls import url
from .views import OrderCreateView

urlpatterns = [
    url('create/', OrderCreateView.as_view(), name='order_create'),
]
