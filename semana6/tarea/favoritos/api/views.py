from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Favorito
from .serializers import FavoritoSerializer

class IndexView(APIView):
    def get(self,request):
        context={'mensaje':'eres un carry'}
        return Response(context)

class FavoritoView(APIView):
    def get(self,request):
        dataFavoritos=Favorito.objects.all()
        serFavorito=FavoritoSerializer(dataFavoritos,many=True)
        return Response(serFavorito.data)

    def post(self,request):
        serFavorito=FavoritoSerializer(data=request.data)
        serFavorito.is_valid(raise_exception=True)
        serFavorito.save()
        return Response(serFavorito.data)

class FavoritoDetailView(APIView):

    def get(self,request,favorito_id):
        dataFavorito=Favorito.objects.get(pk=favorito_id)
        serFavorito=FavoritoSerializer(dataFavorito)
        return Response(serFavorito.data)

    def put(self,request,favorito_id):
        dataFavorito=Favorito.objects.get(pk=favorito_id)
        serFavorito=FavoritoSerializer(dataFavorito,data=request.data)
        serFavorito.is_valid(raise_exception=True)
        serFavorito.save()
        return Response(serFavorito.data)

    def delete(self,request,favorito_id):
        dataFavorito=Favorito.objects.get(pk=favorito_id)
        serFavorito=FavoritoSerializer(dataFavorito)
        dataFavorito.delete()
        return Response(serFavorito.data)