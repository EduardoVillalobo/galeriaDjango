from django import forms
from .models import (Galeria, Photo)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['titulo', 'foto']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'file-upload-default'}),
        }

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }