from django.shortcuts import render, redirect
from io import BytesIO
from .models import Mensaje
from .forms import MensajeForm
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles.storage import staticfiles_storage
from xhtml2pdf import pisa
import requests
import os

# Create your views here.
def obtener_temperatura():
    url = 'http://dataservice.accuweather.com/currentconditions/v1/{ciudad}?apikey={api_key}'
    ciudad = '4700'  # Reemplaza con el nombre de tu ciudad
    api_key = '8Id866MPZc6zZgiFn9DwCfzN1BOn5R3v'  # Reemplaza con tu propia API Key de OpenWeatherMap
    
    url = url.format(ciudad=ciudad, api_key=api_key)
    
    try:
        response = requests.get(url)
        data = response.json()
        if(response.status_code == 503):
            temperatura = "Servicio no disponible." + str(data['Message'])
        else:
            temperatura = str(data[0]['Temperature']['Metric']['Value']) + "°C"
        
        return temperatura
    except requests.exceptions.RequestException as e:
        print('Error al obtener la temperatura:', e)
        return None

def mensaje_list(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.save()
            return redirect("/mensaje")
    else:
        form = MensajeForm()   

    mensajes = Mensaje.objects.all()
    temperatura = obtener_temperatura()
    return render(request, 'mensaje/mensaje_list.html', {'form':form,'listado_mensajes': mensajes, 'temperatura':temperatura})

def mensaje_create(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensaje:mensaje_list')
    else:
        form = MensajeForm()
    return render(request, 'mensaje/mensaje_create.html', {'form': form})

def mensaje_pdf(request, pk):
    mensaje = Mensaje.objects.get(pk=pk)
    template = get_template('mensaje/mensaje_pdf.html')
    context = {'mensaje': mensaje}
    html = template.render(context)

    css_files = ['/galeria/css/style.css', 'galeria/syle.css']
    linked_css = ''.join(f'<link rel="stylesheet" type="text/css" href="{css}>"' for css in css_files)
    html = html.replace('</head>', f'{linked_css}</head>')
    
    # Crear el archivo PDF en memoria
    buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer)

    # Verificar si la generación del PDF fue exitosa
    if not pdf.err:
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f"mensaje_{pk}.pdf")

    # En caso de error, mostrar un mensaje o redirigir a una página de error
    return HttpResponse("Ocurrió un error al generar el PDF")
