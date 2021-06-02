from django.shortcuts import render, redirect
from .models import Book, Author


def index(request):
    return render(request, "index.html")

def books(request):
    context = {
            "all_the_books": Book.objects.all(),
        }
    return render(request, "books.html", context)

def authors(request):
    context = {
            "all_the_authors": Author.objects.all(),
        }
    return render(request, "authors.html", context)

def add_book(request):
    print(request.POST['book_title'])
    book_title_from_form = request.POST['book_title']
    book_desc_from_form = request.POST['book_desc']
    Book.objects.create(title = book_title_from_form, desc = book_desc_from_form)
    return redirect('/books')
    
def add_author(request):
    author_first_name_from_form = request.POST['author_first_name']
    author_last_name_from_form = request.POST['author_last_name']
    author_notes_from_form = request.POST['author_notes']
    Author.objects.create(first_name = author_first_name_from_form, last_name = author_last_name_from_form, notes = author_notes_from_form)
    return redirect('/authors')

def view_book(request, num):
    context = {
            "all_the_books": Book.objects.get(id=num),
            "all_the_authors" : Book.objects.get(id=num).authors.all(),
            "possible_authors" : Author.objects.all()

        }
    return render(request, "book_info.html", context)

def view_author(request, num):
    context = {
            "all_the_authors": Author.objects.get(id=num),
            "all_the_books" : Author.objects.get(id=num).books.all(),
            "possible_books" : Book.objects.all()

        }
    return render(request, "author_info.html", context)

def delete_book(request, num):
    book_to_delete = Book.objects.get(id=int(num))
    book_to_delete.delete()
    return redirect('/books')

def delete_author(request, num):
    author_to_delete = Author.objects.get(id=int(num))
    author_to_delete.delete()
    return redirect('/authors')

def add_book_to_author(request):
    book_id_from_form = int(request.POST['book_for_author'])
    author_id_from_form = int(request.POST['author_id'])
    print(author_id_from_form)
    this_author = Author.objects.get(id=author_id_from_form)
    this_book = Book.objects.get(id=book_id_from_form)
    this_book.authors.add(this_author)
    return redirect(f'/author/{author_id_from_form}')
    
def add_author_to_book(request):
    author_id_from_form = int(request.POST['author_for_book'])
    book_id_from_form = int(request.POST['all_the_books.id'])
    that_book = Book.objects.get(id=book_id_from_form)
    that_author = Author.objects.get(id=author_id_from_form)
    that_author.books.add(that_book)
    return redirect(f'/book/{book_id_from_form}')

