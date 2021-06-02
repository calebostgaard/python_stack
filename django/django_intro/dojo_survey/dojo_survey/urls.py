from django.urls import path, include
    
urlpatterns = [
    path('', include('dojo_survey_app.urls')),
]