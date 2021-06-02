from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.view_shows),
    path('shows/new', views.add_show),
    path('new', views.create),
    path('shows/<int:num>', views.view_show_specific),
    path('shows/<int:num>/edit', views.edit_show),
    path('delete/<int:num>', views.delete),
    path('shows/<int:num>/edit/execute', views.edit_show_execute),
    ]
