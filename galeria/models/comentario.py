from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .photo import Photo

# Create your models here.
from django.utils import timezone
class Comentario(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=450)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.comentario