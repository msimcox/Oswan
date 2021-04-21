from django.shortcuts import render
from .models import Motorcycle
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'index.html', {'motorcycles': motorcycles})

# def detail1(request, motorcycle_id):
#     motorcycle = Motorcycle.objects.get(id=motorcycle_id)
#     return render(request, 'product-details-1.html', {'motorcycle': motorcycle})

def detail2(request, motorcycle_id):
    motorcycle = Motorcycle.objects.get(id=motorcycle_id)
    return render(request, 'product-details-2.html', {'motorcycle': motorcycle})