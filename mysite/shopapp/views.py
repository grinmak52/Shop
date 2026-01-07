from timeit import default_timer
from django.shortcuts import render
from django.http import HttpResponse


def shop_index(request):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products
    }
    return render(request, "shopapp/shop-index.html", context=context)