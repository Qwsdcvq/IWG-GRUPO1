from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'home.html')


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
        return  redirect("signin")
    

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            nombre = user.nombre
            return render(request, "home.html", {"nombre" : nombre})


        else:
            messages.error(request,"Error de confirmacion")
            return redirect("home")


    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Cierre de sesion exitoso")
    return redirect("home")
