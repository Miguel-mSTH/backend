from datetime import datetime
from urllib import response
from django.test import TestCase

# Create your tests here.
from .models import Favorito
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
class FavoritoModelTests(TestCase):
    def test_create_favorito(self):
        """test para validar la creacion de un favorito"""
        fv=Favorito()
        fv.titulo="GOOGLE"
        fv.url="http://www.google.com"
        fv.fecha_registro=timezone.now()
        fv.save()

        self.assertEqual(fv.titulo,"GOOGLE")
        #self.assertEqual(fv.fecha_registro,timezone.now())

class FavoritoAPIViewTests(APITestCase):
    def test_favorito_post(self):
        """prueba de registro de un nuevo favorito enviando por metodo post"""
        url=reverse('api:favoritos')
        data={
            'titulo':'codigo',
            'url':'http://www.codigo.com',
        }

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,200)
        self.assertEqual(Favorito.objects.count(),1)
        self.assertEqual(Favorito.objects.get().titulo,'nuevo favorito')

