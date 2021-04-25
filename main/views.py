from django.shortcuts import render
from .models import Motorcycle
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MotoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import MotoForm, LoginForm

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_motorcycle(request):
    motorcycle_id = request.POST.get('motorcycle_id', None) #?????????????????????????????????????

    likes = 0
    if (motorcycle_id):
        motorcycle = Motorcycle.objects.get(id=int(motorcycle_id))
        if motorcycle is not None:
            likes = motorcycle.likes + 1
            motorcycle.likes = likes
            motorcycle.save()

    return HttpResponse(likes)