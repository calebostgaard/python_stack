from django.shortcuts import render, redirect
from .models import User

def index(request):
    user_list = {
        "all_the_users": User.objects.all()
    }
    return render(request, "index.html", user_list)

def add_user(request):
    first_name_from_form = request.POST['first_name']
    last_name_from_form = request.POST['last_name']
    email_address_from_form = request.POST['email_address']
    age_from_form = request.POST['age']
    User.objects.create(first_name=first_name_from_form, last_name=last_name_from_form, email_address=email_address_from_form, age=int(age_from_form))
    return redirect('/')

def delete_user(request):
    user_from_form = request.POST['delete_user']
    user_to_delete = User.objects.get(id=int(user_from_form))
    user_to_delete.delete()
    return redirect('/')
