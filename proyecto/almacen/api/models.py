from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Presentacion(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    presentacion=models.ForeignKey(Presentacion,on_delete=models.RESTRICT)
    codigo=models.CharField(max_length=200)
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)
    imagen=CloudinaryField('image',default='')

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    razon_social=models.CharField(max_length=200)
    sector_comercial=models.CharField(max_length=200)
    num_documento=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200,blank=True)
    telefono1=models.CharField(max_length=200,blank=True)
    telefono2=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=200,blank=True)
    url=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.razon_social

class Cliente(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.RESTRICT)
    nombre=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200)
    num_documento=models.CharField(max_length=200)
    direcccion=models.CharField(max_length=200,blank=True)
    telefono=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=200,blank=True)

    def __str__(self):
        return self.nombre

class Ingreso(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.RESTRICT)
    fecha=models.DateTimeField()
    serie=models.CharField(max_length=200)

    def __str__(self):
        return self.serie

class DetalleIngreso(models.Model):
    ingreso=models.ForeignKey(Ingreso,on_delete=models.RESTRICT)
    articulo=models.ForeignKey(Articulo,on_delete=models.RESTRICT)
    stock_inicial=models.IntegerField(default=0)
    stock_actual=models.IntegerField(default=0)
    fecha_venc=models.DateTimeField()

    def __str__(self):
        return str(self.stock_actual)

class Salida(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha=models.DateTimeField()
    serie=models.CharField(max_length=200)

    def __str__(self):
        return self.serie

class DetalleSalida(models.Model):
    salida=models.ForeignKey(Salida,on_delete=models.RESTRICT)
    detalle_ing=models.ForeignKey(DetalleIngreso,on_delete=models.RESTRICT)
    cantidad=models.IntegerField(default=1)

    def __str__(self):
        return str(self.cantidad)

