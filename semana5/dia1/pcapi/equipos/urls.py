from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('empleados',views.empleados,name='empeados'),
    path('empleados/set',views.crearEmpleado),
    path('equipos',views.equipos)
]