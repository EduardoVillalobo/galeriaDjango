from django.db import models
from .galeria import Galeria

class Photo(models.Model):
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    foto = models.FileField(upload_to='fotos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo