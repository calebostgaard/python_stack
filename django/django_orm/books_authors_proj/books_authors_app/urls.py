from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book/<int:num>', views.view_book),
    path('author/<int:num>', views.view_author),
    path('delete_book/<int:num>', views.delete_book),
    path('delete_author/<int:num>', views.delete_author),
    path('add_book_to_author', views.add_book_to_author),
    path('add_author_to_book', views.add_author_to_book),

]
