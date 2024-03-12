from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Vendedores)
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Facturas)