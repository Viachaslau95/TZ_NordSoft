from django.contrib import admin
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'price', 'number']
    # ссылка на объект
    list_display_links = ['name']
    # поиск по полям
    search_fields = ['name', 'price']
    # фильтр
    list_filter = ['author']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # ссылка на объект
    list_display_links = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
# tzadmin
