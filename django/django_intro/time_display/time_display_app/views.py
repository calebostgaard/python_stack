from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%B %e, %Y %H:%M %p", gmtime())
    }
    return render(request, 'time_display.html', context)

def timedis(request):
    return redirect("/")