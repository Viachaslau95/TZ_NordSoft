from django.db.models import Q
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics


from shop.models import Book, Author
from shop.forms import BookForm
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from shop.serializers import BookSerializer, AuthorSerializer, BookDetailSerializer
from shop.utils import export_to_csv
from shop.filters import BookFilter


class AllBook(generics.ListAPIView):
    model = Book
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = BookFilter
    queryset = Book.objects.all()


class BookApi(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


class AllAuthors(generics.ListAPIView):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


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


# Добавление новых книг
class CreateBook(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = 'shop/add_book.html'
    success_url = reverse_lazy('home')
    raise_exception = True


class BookDetail(DetailView):
    model = Book
    template_name = 'shop/book_detail.html'


# Поиск книг на сайте
class Search(TemplateView):
    template_name = 'shop/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        results = Book.objects.filter(Q(name__icontains=kw) | Q(description__icontains=kw))
        context['results'] = results
        return context


# Экспорт CSV всех книг
class BooksExportAcCSV(APIView):
    def get(self, request):
        books = get_books_data()
        data = export_to_csv(queryset=books[0], fields=books[1], titles=books[2], file_name=books[3])
        return data


def get_books_data():
    queryset = Book.objects.all()
    fields = ['Название книги', 'Автор книги']
    titles = ['name', 'author']
    file_name = 'Books'
    return queryset, titles, fields, file_name




