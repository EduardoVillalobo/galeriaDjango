from django.shortcuts import render, redirect
from io import BytesIO
from .models import Mensaje
from .forms import MensajeForm
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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
    mensaje = Mensaje.objects.get(pk=pk)
    template = get_template('mensaje/mensaje_pdf.html')
    context = {'mensaje': mensaje}
    html = template.render(context)

    # Crear el archivo PDF en memoria
    buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer)

    # Verificar si la generación del PDF fue exitosa
    if not pdf.err:
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f"mensaje_{pk}.pdf")

    # En caso de error, mostrar un mensaje o redirigir a una página de error
    return HttpResponse("Ocurrió un error al generar el PDF")
