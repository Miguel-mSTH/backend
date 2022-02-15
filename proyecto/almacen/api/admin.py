from django.contrib import admin

# Register your models here.
from .models import Articulo, Categoria, Cliente, DetalleIngreso, DetalleSalida, Ingreso, Presentacion, Proveedor, Salida

admin.site.register(Categoria)
admin.site.register(Presentacion)
admin.site.register(Articulo)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Ingreso)
admin.site.register(DetalleIngreso)
admin.site.register(Salida)
admin.site.register(DetalleSalida)