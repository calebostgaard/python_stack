from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.user_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')

    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hashed_pw)
        new_user = User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            password = hashed_pw,
        )
        request.session['user_id'] = new_user.id
        return redirect("/wall")


def log_in(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/wall")
        messages.error(request, "** Invalid Credentials **")
        return redirect("/")
    messages.error(request, "** Email is not associated with an account, please register **")
    return redirect("/")

def wall(request):
    if "user_id" not in request.session:
        return redirect('/')
    user_id = int(request.session['user_id'])
    context = {
        "specified_user" : User.objects.get(id=user_id),
        "all_the_messages" : Message.objects.all().order_by("-created_at"),
    }
    return render(request, "wall.html", context)

def create_message(request):
    Message.objects.create(
        user = User.objects.get(id=int(request.POST['user_id'])),
        message_text = request.POST['message_text'],
    )
    # new_messsage = Message.objects.last()
    # new_message_id = new_message.id
    return redirect("/wall")

def add_comment(request):
    Comment.objects.create(
        user = User.objects.get(id=int(request.POST['user_id'])),
        message = Message.objects.get(id=int(request.POST['message_id'])),
        comment_text = request.POST['comment_text']
    )
    return redirect("/wall")

def delete_message(request, num):
    message_to_delete = Message.objects.get(id=int(num))
    message_to_delete.delete()
    return redirect('/wall')

def log_out(request):
    del request.session['user_id']
    return redirect('/')