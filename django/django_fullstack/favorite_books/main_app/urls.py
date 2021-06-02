from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('log_in', views.log_in),
    path('books', views.welcome),
    path('add_book', views.add_book),
    path('books/<int:num>', views.view_book),
    path('edit_book/<int:num>', views.edit_book),
    path('delete_book/<int:num>', views.delete_book),
    path('add_to_favorites/<int:num>', views.add_to_favorites),
    path('remove_from_favorites/<int:num>', views.remove_from_favorites),
    path('log_out', views.log_out),
]
