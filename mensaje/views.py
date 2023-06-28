from django.shortcuts import render, redirect
from io import BytesIO
from .models import Mensaje
from .forms import MensajeForm
from django.http import FileResponse
from reportlab.pdfgen import canvas
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

    # Crear el archivo PDF en memoria
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Generar el contenido del PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "Título: " + mensaje.titulo)
    p.drawString(100, 700, "Cuerpo: " + mensaje.cuerpo)

    # Finalizar el PDF
    p.showPage()
    p.save()

    # Reiniciar el buffer de lectura y devolver la respuesta
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"mensaje_{pk}.pdf")
