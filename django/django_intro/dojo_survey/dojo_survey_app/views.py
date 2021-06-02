from django.shortcuts import render, redirect # don't forget to import redirect!

def index(request):
    # this is the route that shows the form
    return render(request,"index.html")

def create_user(request):
    # this is the route that processes the form
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    print(name_from_form)
    print(location_from_form)
    print(language_from_form)
    print(comment_from_form)
    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "language_on_template" : language_from_form,
        "comment_on_template" : comment_from_form,
    }
    return render(request,"show.html", context)

