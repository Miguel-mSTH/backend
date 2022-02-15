from django.urls import path

from . import views

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('categorias',views.CategoriaView.as_view(),name='categorias'),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('presentacion',views.PresentacionView.as_view(),name='presentacion'),
    path('presentacion/<int:presentacion_id>',views.PresentacionDetailView.as_view()),
    path('articulos',views.ArticuloView.as_view(),name='articulos'),
    path('articulo/<int:articulo_id>',views.ArticuloDetailView.as_view()),
    path('proveedores',views.ProveedorView.as_view(),name='proveedores'),
    path('proveedor/<int:proveedor_id>',views.ProveedorDetailView.as_view()),
    path('clientes',views.ClienteView.as_view(),name='clientes'),
    path('cliente/<int:cliente_id>',views.ClienteDetailView.as_view()),
    path('ingresos',views.IngresoView.as_view(),name='ingresos'),
    path('ingreso/<int:ingreso_id>',views.IngresoDetailView.as_view()),
    path('dtingreso',views.DetalleIngresoView.as_view(),name='dtingreso'),
    path('dtingreso/<int:dtingreso_id>',views.DetalleIngresoDetailView.as_view()),
    path('salidas',views.SalidaView.as_view(),name='salidas'),
    path('salida/<int:salida_id>',views.SalidaDetailView.as_view()),
    path('dtsalida',views.DetalleSalidaView.as_view(),name='dtsalida'),
    path('dtsalida/<int:dtsalida_id>',views.DetalleSalidaDetailView.as_view())
]