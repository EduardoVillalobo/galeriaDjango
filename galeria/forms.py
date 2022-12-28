from django import forms
from .models import (Galeria, Photo)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['titulo', 'foto']

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['titulo']