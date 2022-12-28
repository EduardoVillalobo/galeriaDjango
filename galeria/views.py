from django.shortcuts import render
from .models import (Galeria, Photo)
from django.http import (HttpResponseRedirect, JsonResponse)
from django.shortcuts import redirect
from .forms import (GaleriaForm, PhotoForm)

def galeria_list(request):
    listado_galerias = Galeria.objects.all()

    if request.method == 'POST':
        form = GaleriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = GaleriaForm
    return render(request, 'galeria/index.html',{
            'form':form,
            'listado_galerias' : listado_galerias
        })

def model_form_upload(request, pk):
    galeria = Galeria.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():            
            post = form.save(commit=False)
            post.galeria_id = pk
            post.save()
            return redirect('galeria:detail', pk=galeria.id)
    else:
        form = PhotoForm
    return render(request, 'galeria/detail.html',{
        'form': form,
        'galeria': galeria
    })

def delete_galeria(request, pk):
    galeria = Galeria.objects.get(pk=pk)
    galeria.delete()
    return redirect('/')

def delete_photo(request, pk):
    foto = Photo.objects.get(pk=pk)
    galeria = Galeria.objects.get(pk=foto.galeria_id)
    foto.delete()
    return redirect('galeria:detail', galeria.pk)