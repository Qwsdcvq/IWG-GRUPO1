from django import forms
from . models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
#Formulario para los modelos


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username','email','password1','password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields