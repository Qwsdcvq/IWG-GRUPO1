from django.urls import path
from. import views

#Añadir aqui cada una de las URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('mapa/', views.mapa, name='mapa'),
    path('perfil/', views.perfil, name='perfil')
    
]