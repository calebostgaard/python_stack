from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = float(request.POST["specific_id"])
    chosen = Product.objects.get(id = id_from_form)
    price_from_form = float(chosen.price)
    total_charge = quantity_from_form * price_from_form
    if 'total_quantity' in request.session:
        request.session['total_quantity'] += quantity_from_form
    else:
        request.session['total_quantity'] = quantity_from_form
    if 'grand_total' in request.session:
        request.session['grand_total'] += total_charge
    else:
        request.session['grand_total'] = total_charge
    
    request.session['total_charge'] = total_charge
    
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')

def checkout(request):
    return render(request, "store/checkout.html")

def flush(request):
    request.session.flush()
    return redirect('/')
