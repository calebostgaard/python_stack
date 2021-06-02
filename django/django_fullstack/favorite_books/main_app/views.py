from django.shortcuts import render, redirect
from .models import User, Book
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
        return redirect("/books")

def log_in(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/books")
        messages.error(request, "** Invalid Credentials **")
        return redirect("/")
    messages.error(request, "** Email is not associated with an account, please register **")
    return redirect("/")

def welcome(request):
    if "user_id" not in request.session:
        return redirect('/')
    user_id = int(request.session['user_id'])
    context = {
        "specified_user" : User.objects.get(id=user_id),
        "all_the_books" : Book.objects.all(),
        "my_favorites" : Book.objects.filter(users_who_like = User.objects.get(id=user_id))
    }
    return render(request, "welcome.html", context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/books')
    else:
        new_book = Book.objects.create(
            title = request.POST['book_title'],
            desc = request.POST['book_desc'],
            uploaded_by = User.objects.get(id=request.POST['uploaded_by']),
        )
        this_user = User.objects.get(id=request.POST['uploaded_by'])
        this_user.liked_books.add(new_book)	
        return redirect("/books")

def view_book(request, num):
    this_book = Book.objects.get(id=num)
    user_id = int(request.session['user_id'])
    context = {
            "specified_user" : User.objects.get(id=user_id),
            "this_book": Book.objects.get(id=num),
            "all_the_users_who_liked": this_book.users_who_like.all(),
        }
    return render(request, "book_info.html", context)

def edit_book(request, num):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0 and len(errors['unique_book']) == 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/books/{num}')

    else: 
        book_title_from_form = request.POST['book_title']
        book_desc_from_form = request.POST['book_desc']
        book_to_edit = Book.objects.get(id=int(num))
        book_to_edit.title = book_title_from_form
        book_to_edit.desc = book_desc_from_form
        book_to_edit.save()
        return redirect(f'/books/{num}')

def delete_book(request, num):
    this_book = Book.objects.get(id=num)
    this_book.delete()
    return redirect("/books")


def add_to_favorites(request, num):
    this_book = Book.objects.get(id=num)
    this_user = User.objects.get(id = int(request.session['user_id']))
    this_user.liked_books.add(this_book)	
    return redirect(f'/books/{num}')

def remove_from_favorites(request, num):
    this_book = Book.objects.get(id=num)
    this_user = User.objects.get(id = int(request.session['user_id']))
    this_user.liked_books.remove(this_book)	
    return redirect(f'/books/{num}')

def log_out(request):
    del request.session['user_id']
    return redirect('/')