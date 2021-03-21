from django_filters import rest_framework as filters
from shop.models import Book


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = Book
        fields = ['name', 'price']
