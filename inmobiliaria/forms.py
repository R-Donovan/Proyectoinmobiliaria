from django import forms
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo', 'descripcion', 'precio', 'ubicacion', 'no_habitaciones', 'no_banos', 'tamano']
