from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('checkout', views.checkout),
    path('flush', views.flush)
]
