from dataclasses import fields
from wsgiref import validate
from rest_framework import serializers

from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields= '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields='__all__'

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plato
        fields='__all__'

    def to_representation(self,instance):
        representation=super().to_representation(instance)
        representation['plato_img']=instance.plato_img.url
        return representation

class CategoriaPlatosSerializer(serializers.ModelSerializer):
    Platos=PlatoSerializer(many=True,read_only=True)
    class Meta:
        model=Categoria
        fields=['categoria_id','categoria_nom','Platos']

class PedidoPlatoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model=PedidoPlato
        fields=['plato_id','pedidoplato_cant']

class PedidoSerializerPOST(serializers.ModelSerializer):
    PedidoPlatos=PedidoPlatoSerializerPOST(many=True)
    class Meta:
        model=Pedido
        fields=['pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','PedidoPlatos']

    def create(self,validated_data):
        pedidos_data=validated_data.pop('PedidoPlatos')
        pedido=Pedido.objects.create(**validated_data)
        for pedido_data=in pedidos_data:
            PedidoPlato.objects.create(pedido_id=pedido,**pedido_data)
        return pedido
