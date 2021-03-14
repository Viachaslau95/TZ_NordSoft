from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'price']
    # ссылка на объект
    list_display_links = ['name']
    # поиск по полям
    search_fields = ['name', 'price']
    # фильтр
    list_filter = ['author']
    # поля которые можно изменять в админке
    list_editable = ['price']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"')
        else:
            return '-'

    get_photo.short_description = 'Фото'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # ссылка на объект
    list_display_links = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.site_header = 'Управление книгами '
# tzadmin
