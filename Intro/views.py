from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'home.html')

def Login(request):
    print('4')
    return render(request, 'registration/login.html')


def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        print('2')
        if form.is_valid():
            print('3')
            user = form.save()
            messages.success(request,'Cuenta creada con exito')
            return redirect(to='login')

    else:
        form = UserForm()
        print('1')
    return render(request, "registration/signup.html",{'form':form})

def signin(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        username =  form.cleaned_data['username']
        pass1 = form.cleaned_data["password"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            nombre = User.objects.get('username')
            print(nombre)
            return render(request, "home.html", {"nombre1" :nombre })


        else:
            messages.error(request,"Error de confirmacion")
            return redirect("registration/signin")


    return render(request,"registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Cierre de sesion exitoso")
    return redirect("home")

def mapa(request):
    return render(request,"mapa.html")

def perfil(request):
    return render(request, "perfil.html")