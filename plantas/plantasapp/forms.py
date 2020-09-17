from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomerForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    celular = forms.CharField(required=True, label='celular', max_length=10, min_length=10)
    detalle = forms.Textarea()

    def clean_celular(self):
        celular = self.cleaned_data("celular")
        if celular != '' and not celular.isdigit():
            raise forms.ValidationError("Ingrese solo numeros")
        return celular
