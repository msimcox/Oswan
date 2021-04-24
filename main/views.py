from django.shortcuts import render
from .models import Motorcycle
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MotoForm
from django.contrib.auth.models import User

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
        motorcycle = form.save(commit = False)
        motorcycle.user=request.user
        motorcycle.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    motorcycles = Motorcycle.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username,'motorcycles': motorcycles})