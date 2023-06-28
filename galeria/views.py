from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import transaction
from PIL import Image

from .forms import GaleriaForm, PhotoForm, RegisterForm, ComentarioForm
from .models import Galeria, Photo, Comentario

@login_required(login_url="/login")
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
@transaction.atomic
def galeria_list(request):
    if request.method == 'POST':
        form = GaleriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/")
    else:
        form = GaleriaForm()
    
    listado_galerias = Galeria.objects.all()
    return render(request, 'index.html',{
            'form':form,
            'listado_galerias' : listado_galerias
        })

@login_required(login_url="/login")
@transaction.atomic
def galeria_detail(request, pk):
    limit_kb = 150
    galeria = get_object_or_404(Galeria, pk=pk)
    
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
        form = PhotoForm()

    return render(request, 'detail.html',{
        'form': form,
        'galeria': galeria
    })

@login_required(login_url="/login")
@transaction.atomic
def galeria_delete(request, pk):
    galeria = Galeria.objects.get(pk=pk)
    galeria.delete()
    return redirect('/')

@login_required(login_url="/login")
@transaction.atomic
def photo_delete(request, pk):
    foto = Photo.objects.get(pk=pk)
    foto.delete()
    return redirect('galeria:galeria_detail', pk=foto.galeria_id)

@login_required(login_url="/login")
@transaction.atomic
def photo_detail(request, pk):
    foto = get_object_or_404(Photo, pk=pk)
    galeria = get_object_or_404(Galeria, photo = pk)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)    
        try:
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.photo = foto
                post.save()
        except Exception as e:
            messages.error(request, f"Error al guardar el comentario: {str(e)}")
    else:
        form = ComentarioForm()

    return render(request, 'photo_detail.html', {
        'galeria':galeria,
        'photo': foto,
        'form':form
    })