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