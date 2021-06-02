from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages



def index(request):
    return redirect('/shows')

def view_shows(request):
    context = {
        "all_the_shows": Show.objects.all(),
        }
    return render(request, "view_shows.html", context)

def add_show(request):
    return render(request, "add_show.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')

    else: 
        show_title_from_form = request.POST['show_title']
        show_network_from_form = request.POST['show_network']
        show_release_date_from_form = request.POST['show_release_date']
        show_desc_from_form = request.POST['show_desc']
        Show.objects.create(title = show_title_from_form, network = show_network_from_form, release_date=show_release_date_from_form, desc = show_desc_from_form)
        new_show = Show.objects.last()
        new_id = new_show.id
        return redirect(f'/shows/{new_id}')



def view_show_specific(request, num):
    context = {
            "specific_show": Show.objects.get(id=num),
        }
    return render(request, "view_specifc_show.html", context)

def edit_show(request, num):
    this_show = Show.objects.get(id=num)
    date = this_show.release_date.strftime("%Y-%m-%d")
    context = {
            "specific_show": Show.objects.get(id=num),
            "date" : date
    }
    return render(request, "edit_show.html", context)

def delete(request, num):
    show_to_delete = Show.objects.get(id=int(num))
    show_to_delete.delete()
    return redirect('/shows')

def edit_show_execute(request, num):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0 and len(errors['show_unique_title']) == 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{num}/edit')

    else: 
        show_title_from_form = request.POST['show_title']
        show_network_from_form = request.POST['show_network']
        show_release_date_from_form = request.POST['show_release_date']
        show_desc_from_form = request.POST['show_desc']
        show_to_edit = Show.objects.get(id=int(num))
        show_to_edit.title = show_title_from_form
        show_to_edit.network = show_network_from_form
        show_to_edit.release_date = show_release_date_from_form
        show_to_edit.desc = show_desc_from_form
        show_to_edit.save()
        return redirect(f'/shows/{num}')
