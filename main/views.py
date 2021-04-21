from django.shortcuts import render
from .models import Motorcycle
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MotoForm

def index(request):
    motorcycles = Motorcycle.objects.all()
    form = MotoForm()
    return render(request, 'index.html', {'motorcycles': motorcycles, 'form':form})

# def detail1(request, motorcycle_id):
#     motorcycle = Motorcycle.objects.get(id=motorcycle_id)
#     return render(request, 'product-details-1.html', {'motorcycle': motorcycle})

def detail2(request, motorcycle_id):
    motorcycle = Motorcycle.objects.get(id=motorcycle_id)
    return render(request, 'product-details-2.html', {'motorcycle': motorcycle})

def post_moto(request):
    form = MotoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True) # In this single line: read all data on form and submit to database
    return HttpResponseRedirect('/')

