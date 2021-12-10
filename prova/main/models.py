from datetime import datetime as dt
from django.db import models

# Create your models here.
class filme(models.Model):

    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data = models.DateTimeField("Publicado em", default=dt.now())

    def __str__(self):
        return self.titulo
