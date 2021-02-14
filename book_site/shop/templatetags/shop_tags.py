from django import template
from django.db.models import Count

from shop.models import Author

register = template.Library()


@register.inclusion_tag('shop/list_authors.html')
def show_authors():
    authors = Author.objects.annotate(cnt=Count('book')).filter(cnt__gt=0)

    return {'authors': authors}

