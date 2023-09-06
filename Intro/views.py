from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})





