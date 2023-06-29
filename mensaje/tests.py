from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Mensaje


class MensajeViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_mensaje_list_view(self):
        url = reverse("mensaje:mensaje_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mensaje/mensaje_list.html')

    def test_mensaje_create_view(self):
        url = reverse('mensaje:mensaje_create')
        data = {
            'titulo': 'Nuevo mensaje',
            'cuerpo': 'Este es un nuevo mensaje.',
        }
        
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mensaje:mensaje_list'))

        # Verificar que se haya creado el mensaje
        self.assertEqual(Mensaje.objects.count(), 1)
        mensaje = Mensaje.objects.first()
        self.assertEqual(mensaje.titulo, 'Nuevo mensaje')
    
    def test_mensaje_pdf_view(self):
        mensaje = Mensaje.objects.create(
            titulo='Test mensaje',
            cuerpo='Este es un mensaje de prueba.'
        )
        url = reverse('mensaje:mensaje_pdf', args=[mensaje.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
    
    def test_mensaje_pdf_view_error(self):
        # Prueba cuando ocurre un error al generar el PDF
        mensaje = Mensaje.objects.create(
            titulo='Test mensaje',
            cuerpo='Este es un mensaje de prueba.'
        )
        url = reverse('mensaje:mensaje_pdf', args=[mensaje.pk])

        with self.assertRaises(Exception):
            # Simular un error al pasar un objeto incorrecto a pisa.pisaDocument
            with patch('mensaje.views.pisa.pisaDocument') as mock_pisa:
                mock_pisa.side_effect = Exception('Error al generar el PDF')
                response = self.client.get(url)
                self.assertEqual(response.status_code, 500)