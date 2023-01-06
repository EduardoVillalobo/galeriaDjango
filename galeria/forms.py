from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Galeria, Photo

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']

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
