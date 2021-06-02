from django.shortcuts import render, redirect # don't forget to import redirect!
import  random # don't forget to import redirect!

def index(request):
    if 'randomnumber' not in request.session:
        request.session['randomnumber'] = random.randint(1, 100)
        print(request.session['randomnumber'])
    else:
        print(request.session['randomnumber'])
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request,"index.html")

def submit(request):
    message = " "
    request.session['guess'] = int(request.POST['guess'])
    # if request.POST['guess'] is not an integer:
    #     return redirect("/")
    if request.session['counter'] >= 4:
        message = "You Lose"
        request.session['color'] = "rgb(255, 121, 0)"
    else:
        if int(request.POST['guess']) < request.session['randomnumber']:
            message = "Too Low"
            request.session['color'] = "rgb(255, 132, 132)"
        if int(request.POST['guess']) > request.session['randomnumber']:
            message = "Too High"
            request.session['color'] = "rgb(155, 0, 0)"
        if int(request.POST['guess']) == request.session['randomnumber']:
            message = f"{request.session['randomnumber']} was the number!"
            request.session['color'] = "green"
    request.session['counter'] += 1
    print(request.session['counter'])
    request.session['message'] = message
    return redirect("/")

def playagain(request):
    request.session.flush()
    return redirect("/")




