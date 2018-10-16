# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Product

# the index function is called when root is visited

def index(request):
    print("index()")

    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkout(request):
    print("checkout()")

    context = request.session['record']

    return render(request, "order.html", context)

def process_order(request):
    print("process_order()")

    if request.method == "POST":
        if "record" in request.session:
            running_total = request.session['record']['running_total']
            total_orders = request.session['record']['total_orders']
        else:
            running_total = 0
            total_orders = 0

        quantity_purchased = request.POST["quantity"]
        obj_item_purchased = Product.objects.get(id=request.POST["product_id"])
        purchase_total = float(quantity_purchased) * float(obj_item_purchased.unit_price)
        total_orders += int(quantity_purchased)
        running_total = running_total + purchase_total
        
    context = {
        "total_orders": total_orders,
        "total_price": float("{0:.2f}".format(purchase_total)),
        "running_total": float("{0:.2f}".format(running_total))
    }

    request.session['record'] = context

    return redirect(checkout)        