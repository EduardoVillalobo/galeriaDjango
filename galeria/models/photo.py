from django.db import models
from django.contrib.auth.models import User
from .galeria import Galeria

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    foto = models.FileField(upload_to='fotos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo