from dataclasses import field, fields
from rest_framework import serializers

from .models import Articulo, Categoria, Cliente, DetalleIngreso, DetalleSalida, Ingreso, Presentacion, Proveedor, Salida

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'

class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Presentacion
        fields='__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articulo
        fields='__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proveedor
        fields='__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingreso
        fields='__all__'

class DetalleIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleIngreso
        fields='__all__'

class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salida
        fields='__all__'

class DetalleSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleSalida
        fields='__all__'