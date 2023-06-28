from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit
# Create your views here.

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
    return render(request, 'mensaje/mensaje_list.html', {'form':form,'listado_mensajes': mensajes})

def mensaje_create(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensaje_list')
    else:
        form = MensajeForm()
    return render(request, 'mensaje/mensaje_create.html', {'form': form})

def mensaje_pdf(request, pk):
    path_wh = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wh)
    mensaje = Mensaje.objects.get(pk=pk)
    template = get_template('mensaje/mensaje_pdf.html')
    html = template.render({'mensaje': mensaje})
    options = {'page-size': 'A4', 'orientation': 'Landscape'}
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="mensaje_{pk}.pdf"'
    response.write(pdf)
    return response
