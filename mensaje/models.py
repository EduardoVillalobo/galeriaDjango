from django.db import models

class Mensaje(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()

    def __str__(self):
        return self.titulo