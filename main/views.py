from django.shortcuts import render
from .models import Motorcycle

def index(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'index.html', {'motorcycles': motorcycles})

# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')