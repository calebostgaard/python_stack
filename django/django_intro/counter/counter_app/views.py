from django.shortcuts import render, redirect # don't forget to import redirect!

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    return render(request,"index.html")

def addtwo(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    return redirect("/")

def destroy(request):
    del request.session['counter']
    return redirect("/")
