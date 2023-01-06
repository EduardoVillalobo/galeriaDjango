from django.shortcuts import render, redirect
from django.http import (HttpResponseRedirect, JsonResponse)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from PIL import Image

from .forms import GaleriaForm, PhotoForm, RegisterForm
from .models import (Galeria, Photo)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form": form})
        
@login_required(login_url="/login")
def galeria_list(request):
    listado_galerias = Galeria.objects.all()
    if request.method == 'POST':
        form = GaleriaForm(request.POST)
        
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            import pdb; pdb.set_trace()
            post.save()
            return HttpResponseRedirect("/")
    else:
        form = GaleriaForm
    
    return render(request, 'index.html',{
            'form':form,
            'listado_galerias' : listado_galerias
        })

@login_required(login_url="/login")
def galeria_detail(request, pk):
    
    galeria = Galeria.objects.get(pk=pk)
    limit_kb = 150
    if request.method == 'POST':
        try:
            file = request.FILES['foto']
            image = Image.open(file)
            image.verify()
            
            if file.size > limit_kb * 1024:
                messages.error(request, "Limite excedido. Máximo de 150kb")
                return redirect('galeria:galeria_detail', pk=galeria.id)
        except:
            messages.error(request, "El archivo no corresponde a una imagen.")
            return redirect('galeria:galeria_detail', pk=galeria.id)

        form = PhotoForm(request.POST, request.FILES)
        
        if form.is_valid():            
            post = form.save(commit=False)
            post.author = request.user
            post.galeria_id = pk
            post.save()
            return redirect('galeria:galeria_detail', pk=galeria.id)
    else:
        form = PhotoForm
    return render(request, 'detail.html',{
        'form': form,
        'galeria': galeria
    })

@login_required(login_url="/login")
def galeria_delete(request, pk):
    galeria = Galeria.objects.get(pk=pk)
    galeria.delete()
    return redirect('/')

@login_required(login_url="/login")
def photo_delete(request, pk):
    foto = Photo.objects.get(pk=pk)
    foto.delete()
    return redirect('galeria:galeria_detail', Galeria.objects.get(pk=foto.galeria_id).pk)