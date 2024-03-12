from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('vendedores/', vendedores, name="vendedores"),
    path('clientes/', clientes, name="clientes"),
    path('productos/', productos, name="productos"),
    path('facturas/', facturas, name="facturas"),
    #--------------formularios--------------
    path('vendedores_form/', vendedoresForm, name="vendedores_form"),
    path('clientes_form/', clientesForm, name="clientes_form"),
    path('productos_form/', productosForm, name="productos_form"),
    path('facturas_form/', facturasForm, name="facturas_form"),
    #---------------buscador-----------------
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),
]