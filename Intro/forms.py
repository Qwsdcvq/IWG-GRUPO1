from django import forms
from . models import User

#Formulario para los modelos

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nombre_usuario',
            'nombre',
            'email',
            'patente',
            
        ]