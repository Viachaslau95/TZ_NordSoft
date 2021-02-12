from django.urls import path
from .views import index, get_author

urlpatterns = [
    path('', index, name='home'),
    path('author/<int:author_id>', get_author, name='author')

]
 # смотреть 19 урок