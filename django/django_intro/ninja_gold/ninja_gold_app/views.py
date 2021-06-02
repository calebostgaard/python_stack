from django.shortcuts import render, redirect
import  random # don't forget to import redirect!
import datetime

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
        request.session['activity'] = ""
        print(request.session['gold_count'])
    else: 
        request.session['gold_count']
        request.session['activity']
    return render(request,"index.html")

def process_money(request):
    timestamp = "{:%b, %d %Y - %H:%M:%S}".format(datetime.datetime.now())
    if request.POST['find_gold'] == 'farm':
        rando = random.randint(10, 20)
        request.session['activity'] = "<p style= 'color: green'>Earned " + str(rando) + " golds from the " + str(request.POST['find_gold']) + " (" + timestamp + ")</p>" + request.session['activity']
    elif request.POST['find_gold'] == 'cave':
        rando = random.randint(5, 10)
        request.session['activity'] = "<p style= 'color: green'>Earned " + str(rando) + " golds from the " + str(request.POST['find_gold']) + " (" + timestamp + ")</p>" + request.session['activity']
    elif request.POST['find_gold'] == 'house':
        rando = random.randint(2, 5)
        request.session['activity'] = "<p style= 'color: green'>Earned " + str(rando) + " golds from the " + str(request.POST['find_gold']) + " (" + timestamp + ")</p>" + request.session['activity']
    elif request.POST['find_gold'] == 'casino':
        rando = random.randint(-50, 50)
        if rando >= 0:
            request.session['activity'] = "<p style= 'color: green'>Entered a casino and earned " + str(rando) + " golds... Woohoo! " + " (" + timestamp + ")</p>" + request.session['activity']
        else:
            request.session['activity'] = "<p style= 'color: red'>Entered a casino and lost " + str(abs(rando)) + " golds... Ouch! " + " (" + timestamp + ")</p>" + request.session['activity']
    request.session['gold_count'] += rando
    return redirect("/")

def start_over(request):
    request.session.flush()
    return redirect("/")
