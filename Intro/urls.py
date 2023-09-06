from django.urls import path
from. import views

#Añadir aqui cada una de las URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('Login/', views.Login, name =  'Login'),
    
]