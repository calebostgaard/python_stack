from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('log_in', views.log_in),
    path('success', views.success),
    path('log_out', views.log_out),
    path('users', views.users),
    path('delete/<int:num>', views.delete),
    ]
