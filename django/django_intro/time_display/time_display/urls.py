from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete

urlpatterns = [
    path('', include('time_display_app.urls')),
]