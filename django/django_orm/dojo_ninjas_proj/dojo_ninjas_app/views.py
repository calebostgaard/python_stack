from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def index(request):
    dojo_list = {
            "all_the_dojos": Dojo.objects.all(),
            "ninja_count" : Ninja.objects.all().count()

        }
    return render(request, "index.html", dojo_list)
    
def add_dojo(request):
    dojo_name_from_form = request.POST['dojo_name']
    dojo_city_from_form = request.POST['dojo_city']
    dojo_state_from_form = request.POST['dojo_state']
    Dojo.objects.create(name = dojo_name_from_form, city = dojo_city_from_form, state = dojo_state_from_form, desc = " ")   
    return redirect('/')

def add_ninja(request):
    ninja_first_name_from_form = request.POST['ninja_first_name']
    ninja_last_name_from_form = request.POST['ninja_last_name']
    dojo_id_from_form = request.POST['dojo_id']
    Ninja.objects.create(dojo=Dojo.objects.get(id=int(dojo_id_from_form)), first_name=ninja_first_name_from_form, last_name=ninja_last_name_from_form)
    return redirect('/')

def delete_dojo(request):
    dojo_from_form = request.POST['delete_it']
    dojo_to_delete = Dojo.objects.get(id=int(dojo_from_form))
    dojo_to_delete.delete()
    return redirect('/')