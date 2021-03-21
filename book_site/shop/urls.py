from django.urls import path
from .views import HomeBooks, BooksByAuthor, \
    CreateBook, BookDetail, \
    AllBook, AllAuthors, \
    BookApi, Search, BooksExportAcCSV

urlpatterns = [
    path('', HomeBooks.as_view(), name='home'),
    # path('stat/', stat_all_book, name='stat'),
    path('author/<int:author_id>', BooksByAuthor.as_view(), name='author'),
    path('book/add-book', CreateBook.as_view(), name='add_book'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('search/', Search.as_view(), name='search'),
    path('books/', AllBook.as_view(), name='book-list'),
    path('books/<int:pk>', BookApi.as_view(), name='book-list'),
    path('authors/', AllAuthors.as_view(), name='author-list'),
    path('api/users-csv-export/', BooksExportAcCSV.as_view(), name='export')
]
