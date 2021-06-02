from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')

    else:
        hashed_pw = bcrypt.hashpw(request.POST['inputPassword'].encode(), bcrypt.gensalt()).decode()
        print(hashed_pw)
        new_user = User.objects.create(
            first_name = request.POST['inputFirstName'],
            last_name = request.POST['inputLastName'],
            email = request.POST['inputEmail'],
            password = hashed_pw,
            birthday = request.POST['inputBirthday'],
        )
        request.session['user_id'] = new_user.id
        return redirect("/success")


def log_in(request):
    user = User.objects.filter(email = request.POST['inputEmail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['inputPassword'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/success")
        messages.error(request, "** Invalid Credentials **")
        return redirect("/")
    messages.error(request, "** Email is not associated with an account, please register **")
    return redirect("/")

def success(request):
    if "user_id" not in request.session:
        return redirect('/')
    user_id = int(request.session['user_id'])
    context = {
        "specified_user" : User.objects.get(id=user_id)
    }
    return render(request, "success.html", context)



def log_out(request):
    del request.session['user_id']
    return redirect('/')

def users(request):
    context = {
        "all_the_users" : User.objects.all()
    }
    return render(request, "users.html", context)

def delete(request, num):
    user_to_delete = User.objects.get(id=int(num))
    user_to_delete.delete()
    return redirect('/users')