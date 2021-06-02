from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('log_in', views.log_in),
    path('wall', views.wall),
    path('create_message', views.create_message),
    path('add_comment', views.add_comment),
    path('delete_message/<int:num>', views.delete_message),
    path('log_out', views.log_out),
]
