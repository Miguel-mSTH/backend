from django.urls import path

from . import views

app_name='api'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('favoritos',views.FavoritoView.as_view(),name='favoritos'),
    path('favorito/<int:favorito_id>',views.FavoritoDetailView.as_view())
]