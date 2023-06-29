from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


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
