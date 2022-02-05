from django.db import models

# Create your models here.
class Favorito(models.Model):
    titulo=models.CharField(max_length=100)
    url=models.CharField(max_length=200)
    fecha_registro=models.DateField()

    def __str__(self):
        return self.titulo