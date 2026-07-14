from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class BusquedaCategoriaFormulario(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="-- Selecciona una categoría --",
        label="Categoría"
    )