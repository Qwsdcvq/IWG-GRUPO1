from django import forms
from . models import User

#Formulario para los modelos

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    puntos = forms.IntegerField(disabled=True, required=False)
    class Meta:
        model = User
        fields = "__all__"