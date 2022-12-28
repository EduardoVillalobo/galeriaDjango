from django.db import models
from django.http import JsonResponse
from django.utils import timezone


# Create your models here.
from django.utils import timezone

class Galeria(models.Model):
    titulo = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.titulo

class Photo(models.Model):
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    foto = models.FileField(upload_to='fotos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo