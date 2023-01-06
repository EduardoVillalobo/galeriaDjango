from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
from django.utils import timezone
class Galeria(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.titulo