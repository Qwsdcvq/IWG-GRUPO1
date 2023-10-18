from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')


def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        patente = request.POST["patente"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        usuario = User.objects.create_user(username, email, pass1)
        usuario.nombre = nombre

        usuario.save()

        messages.success(request, "Cuenta creada con exito.")
        return redirect(to="login")
    

    return render(request, "registration/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            nombre1 = user.nombre
            return render(request, "home.html", {"nombre1" : nombre1})


        else:
            messages.error(request,"Error de confirmacion")
            return redirect("registration/signin")


    return render(request,"registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Cierre de sesion exitoso")
    return redirect("home")
