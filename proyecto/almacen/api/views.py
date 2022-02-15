from ast import Delete
from re import A
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Articulo, Categoria, Cliente, DetalleIngreso, DetalleSalida, Ingreso, Presentacion, Proveedor, Salida
from .serializers import ArticuloSerializer, CategoriaSerializer, ClienteSerializer, DetalleIngresoSerializer, DetalleSalidaSerializer, IngresoSerializer, PresentacionSerializer, ProveedorSerializer, SalidaSerializer

from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={'ok':'server is running'}
        return Response(context)

class CategoriaView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataCategoria=Categoria.objects.all()
        serCategoria=CategoriaSerializer(dataCategoria,many=True)
        return Response(serCategoria.data)

    def post(self,request):
        serCategoria=CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)

class CategoriaDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,categoria_id):
        dataCategoria=Categoria.objects.get(pk=categoria_id)
        serCategoria=CategoriaSerializer(dataCategoria)
        return Response(serCategoria.data)

    def put(self,request,categoria_id):
        dataCategoria=Categoria.objects.get(pk=categoria_id)
        serCategoria=CategoriaSerializer(dataCategoria,data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)

    def delete(self,request,categoria_id):
        dataCategoria=Categoria.objects.get(pk=categoria_id)
        serCategoria=CategoriaSerializer(dataCategoria)
        dataCategoria.delete()
        return Response(serCategoria.data)

class PresentacionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataPresentacion=Presentacion.objects.all()
        serPresentacion=PresentacionSerializer(dataPresentacion,many=True)
        return Response(serPresentacion.data)

    def post(self,request):
        serPresentacion=PresentacionSerializer(data=request.data)
        serPresentacion.is_valid(raise_exception=True)
        serPresentacion.save()
        return Response(serPresentacion.data)

class PresentacionDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,presentacion_id):
        dataPresentacion=Presentacion.objects.get(pk=presentacion_id)
        serPresentacion=PresentacionSerializer(dataPresentacion)
        return Response(serPresentacion.data)

    def put(self,request,presentacion_id):
        dataPresentacion=Presentacion.objects.get(pk=presentacion_id)
        serPresentacion=PresentacionSerializer(dataPresentacion,data=request.data)
        serPresentacion.is_valid(raise_exception=True)
        serPresentacion.save()
        return Response(serPresentacion.data)

    def delete(self,request,presentacion_id):
        dataPresentacion=Presentacion.objects.get(pk=presentacion_id)
        serPresentacion=PresentacionSerializer(dataPresentacion)
        dataPresentacion.delete()
        return Response(serPresentacion.data)

class ArticuloView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataArticulo=Articulo.objects.all()
        serArticulo=ArticuloSerializer(dataArticulo,many=True)
        return Response(serArticulo.data)

    def post(self,request):
        serArticulo=ArticuloSerializer(data=request.data)
        serArticulo.is_valid(raise_exception=True)
        serArticulo.save()
        return Response(serArticulo.data)

class ArticuloDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,articulo_id):
        dataArticulo=Articulo.objects.get(pk=articulo_id)
        serArticulo=ArticuloSerializer(dataArticulo)
        return Response(serArticulo.data)

    def put(self,request,articulo_id):
        dataArticulo=Articulo.objects.get(pk=articulo_id)
        serArticulo=ArticuloSerializer(dataArticulo,data=request.data)
        serArticulo.is_valid(raise_exception=True)
        serArticulo.save()
        return Response(serArticulo.data)

    def delete(self,request,articulo_id):
        dataArticulo=Articulo.objects.get(pk=articulo_id)
        serArticulo=ArticuloSerializer(dataArticulo)
        dataArticulo.delete()
        return Response(serArticulo.data)

class ProveedorView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataProveedor=Proveedor.objects.all()
        serProveedor=ProveedorSerializer(dataProveedor,many=True)
        return Response(serProveedor.data)

    def post(self,request):
        serProveedor=ProveedorSerializer(data=request.data)
        serProveedor.is_valid(raise_exception=True)
        serProveedor.save()
        return Response(serProveedor.data)

class ProveedorDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,proveedor_id):
        dataProveedor=Proveedor.objects.get(pk=proveedor_id)
        serProveedor=ProveedorSerializer(dataProveedor)
        return Response(serProveedor.data)

    def put(self,request,proveedor_id):
        dataProveedor=Proveedor.objects.get(pk=proveedor_id)
        serProveedor=ProveedorSerializer(dataProveedor,data=request.data)
        serProveedor.is_valid(raise_exception=True)
        serProveedor.save()
        return Response(serProveedor.data)

    def delete(self,request,proveedor_id):
        dataProveedor=Proveedor.objects.get(pk=proveedor_id)
        serProveedor=ProveedorSerializer(dataProveedor)
        dataProveedor.delete()
        return Response(serProveedor.data)

class ClienteView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataCliente=Cliente.objects.all()
        serCliente=ClienteSerializer(dataCliente,many=True)
        return Response(serCliente.data)

    def post(self,request):
        serCliente=ClienteSerializer(data=request.data)
        serCliente.is_valid(raise_exception=True)
        serCliente.save()
        return Response(serCliente.data)

class ClienteDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,cliente_id):
        dataCliente=Cliente.objects.get(pk=cliente_id)
        serCliente=ClienteSerializer(dataCliente)
        return Response(serCliente.data)

    def put(self,request,cliente_id):
        dataCliente=Cliente.objects.get(pk=cliente_id)
        serCliente=ClienteSerializer(dataCliente,data=request.data)
        serCliente.is_valid(raise_exception=True)
        serCliente.save()
        return Response(serCliente.data)

    def delete(self,request,cliente_id):
        dataCliente=Cliente.objects.get(pk=cliente_id)
        serCliente=ClienteSerializer(dataCliente)
        dataCliente.delete()
        return Response(serCliente.data)

class IngresoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataIngreso=Ingreso.objects.all()
        serIngreso=IngresoSerializer(dataIngreso,many=True)
        return Response(serIngreso.data)

    def post(self,request):
        serIngreso=IngresoSerializer(data=request.data)
        serIngreso.is_valid(raise_exception=True)
        serIngreso.save()
        return Response(serIngreso.data)

class IngresoDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,ingreso_id):
        dataIngreso=Ingreso.objects.get(pk=ingreso_id)
        serIngreso=IngresoSerializer(dataIngreso)
        return Response(serIngreso.data)

    def put(self,request,ingreso_id):
        dataIngreso=Ingreso.objects.get(pk=ingreso_id)
        serIngreso=IngresoSerializer(dataIngreso,data=request.data)
        serIngreso.is_valid(raise_exception=True)
        serIngreso.save()
        return Response(serIngreso.data)

    def delete(self,request,ingreso_id):
        dataIngreso=Ingreso.objects.get(pk=ingreso_id)
        serIngreso=IngresoSerializer(dataIngreso)
        dataIngreso.delete()
        return Response(serIngreso.data)

class DetalleIngresoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataDetalleIngreso=DetalleIngreso.objects.all()
        serDetalleIngreso=DetalleIngresoSerializer(dataDetalleIngreso,many=True)
        return Response(serDetalleIngreso.data)

    def post(self,request):
        serDetalleIngreso=DetalleIngresoSerializer(data=request.data)
        serDetalleIngreso.is_valid(raise_exception=True)
        serDetalleIngreso.save()
        return Response(serDetalleIngreso.data)

class DetalleIngresoDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,dtingreso_id):
        dataDetalleIngreso=DetalleIngreso.objects.get(pk=dtingreso_id)
        serDetalleIngreso=DetalleIngresoSerializer(dataDetalleIngreso)
        return Response(serDetalleIngreso.data)

    def put(self,request,dtingreso_id):
        dataDetalleIngreso=DetalleIngreso.objects.get(pk=dtingreso_id)
        serDetalleIngreso=DetalleIngresoSerializer(dataDetalleIngreso,data=request.data)
        serDetalleIngreso.is_valid(raise_exception=True)
        serDetalleIngreso.save()
        return Response(serDetalleIngreso.data)

    def delete(self,request,dtingreso_id):
        dataDetalleIngreso=DetalleIngreso.objects.get(pk=dtingreso_id)
        serDetalleIngreso=DetalleIngresoSerializer(dataDetalleIngreso)
        dataDetalleIngreso.delete()
        return Response(serDetalleIngreso.data)

class SalidaView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataSalida=Salida.objects.all()
        serSalida=SalidaSerializer(dataSalida,many=True)
        return Response(serSalida.data)

    def post(self,request):
        serSalida=SalidaSerializer(data=request.data)
        serSalida.is_valid(raise_exception=True)
        serSalida.save()
        return Response(serSalida.data)

class SalidaDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,salida_id):
        dataSalida=Salida.objects.get(pk=salida_id)
        serSalida=SalidaSerializer(dataSalida)
        return Response(serSalida.data)

    def put(self,request,salida_id):
        dataSalida=Salida.objects.get(pk=salida_id)
        serSalida=SalidaSerializer(dataSalida,data=request.data)
        serSalida.is_valid(raise_exception=True)
        serSalida.save()
        return Response(serSalida.data)

    def delete(self,request,salida_id):
        dataSalida=Salida.objects.get(pk=salida_id)
        serSalida=SalidaSerializer(dataSalida)
        dataSalida.delete()
        return Response(serSalida.data)

class DetalleSalidaView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataDetalleSalida=DetalleSalida.objects.all()
        serDetalleSalida=DetalleSalidaSerializer(dataDetalleSalida,many=True)
        return Response(serDetalleSalida.data)

    def post(self,request):
        serDetalleSalida=DetalleSalidaSerializer(data=request.data)
        serDetalleSalida.is_valid(raise_exception=True)
        serDetalleSalida.save()
        return Response(serDetalleSalida.data)

class DetalleSalidaDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,dtsalida_id):
        dataDetalleSalida=DetalleSalida.objects.get(pk=dtsalida_id)
        serDetalleSalida=DetalleSalidaSerializer(dataDetalleSalida)
        return Response(serDetalleSalida.data)

    def put(self,request,dtsalida_id):
       dataDetalleSalida=DetalleSalida.objects.get(pk=dtsalida_id)
       serDetalleSalida=DetalleSalidaSerializer(dataDetalleSalida,data=request.data)
       serDetalleSalida.is_valid(raise_exception=True)
       serDetalleSalida.save()
       return Response(serDetalleSalida.data)

    def delete(self,request,dtsalida_id):
        dataDetalleSalida=DetalleSalida.objects.get(pk=dtsalida_id)
        serDetalleSalida=DetalleSalidaSerializer(dataDetalleSalida)
        dataDetalleSalida.delete()
        return Response(serDetalleSalida.data)