from django.urls import path
from .views import HomeBooks, BooksByAuthor, CreateBook, book_detail

urlpatterns = [
    path('', HomeBooks.as_view(), name='home'),
    path('author/<int:author_id>', BooksByAuthor.as_view(), name='author'),
    path('book/add-book', CreateBook.as_view(), name='add_book'),
    path('book/<int:id>', book_detail, name='book_detail'),

]
