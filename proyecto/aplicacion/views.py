from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def vendedores(request):
    contexto = {'vendedores': Vendedores.objects.all()}
    return render(request, "aplicacion/vendedores.html", contexto)

def clientes(request):
    contexto = {'clientes': Clientes.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

def productos(request):
    contexto = {'productos': Productos.objects.all()}
    return render(request, "aplicacion/productos.html", contexto)

def facturas(request):
    contexto = {'facturas': Facturas.objects.all()}
    return render(request, "aplicacion/facturas.html", contexto)

#-----------FORMULARIOS-----------
def vendedoresForm(request):
    if request.method == "POST":
        miForm = VendedoresForm(request.POST)
        if miForm.is_valid():
            vendedor_nombre = miForm.cleaned_data.get("nombre")
            vendedor_apellido = miForm.cleaned_data.get("apellido")
            vendedor_correo = miForm.cleaned_data.get("correo")
            vendedor_fechaInicio = miForm.cleaned_data.get("fechaInicio")
            vendedor_venta = miForm.cleaned_data.get("venta")
            vendedor = Vendedores(nombre=vendedor_nombre, apellido=vendedor_apellido, correo=vendedor_correo, fechaInicio=vendedor_fechaInicio, venta=vendedor_venta)
            vendedor.save()

            contexto = {'vendedores': Vendedores.objects.all()}
            return render(request, "aplicacion/vendedores.html", contexto)
    else:
        miForm = VendedoresForm()
        
    return render(request, "aplicacion/vendedoresForm.html", {"form": miForm})

def clientesForm(request):
    if request.method == "POST":
        miForm = ClientesForm(request.POST)
        if miForm.is_valid():
            clientes_nombre = miForm.cleaned_data.get("nombre")
            clientes_apellido = miForm.cleaned_data.get("apellido")
            clientes_correo = miForm.cleaned_data.get("correo")
            clientes_fechaInicio = miForm.cleaned_data.get("fechaInicio")
            clientes_compra = miForm.cleaned_data.get("compra")
            clientes = Clientes(nombre=clientes_nombre, apellido=clientes_apellido, correo=clientes_correo, fechaInicio=clientes_fechaInicio, compra=clientes_compra)
            clientes.save()
            
            contexto = {'clientes': Clientes.objects.all()}
            return render(request, "aplicacion/clientes.html", contexto)
    else:
        miForm = ClientesForm()
        
    return render(request, "aplicacion/clientesForm.html", {"form": miForm})

def productosForm(request):
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            productos_nombre = miForm.cleaned_data.get("nombre")
            productos_vendedor = miForm.cleaned_data.get("vendedor")
            productos_fechaRegistro = miForm.cleaned_data.get("fechaRegistro")
            productos_costo = miForm.cleaned_data.get("costo")
            productos = Productos(nombre=productos_nombre, vendedor=productos_vendedor, fechaRegistro=productos_fechaRegistro, costo=productos_costo)
            productos.save()
            
            contexto = {'productos': Productos.objects.all()}
            return render(request, "aplicacion/productos.html", contexto)
    else:
        miForm = ProductosForm()
        
    return render(request, "aplicacion/productosForm.html", {"form": miForm})

def facturasForm(request):
    if request.method == "POST":
        miForm = FacturasForm(request.POST)
        if miForm.is_valid():
            facturas_nombreProducto = miForm.cleaned_data.get("nombreProducto")
            facturas_nombreVendedor = miForm.cleaned_data.get("nombreVendedor")
            facturas_nombreCliente = miForm.cleaned_data.get("nombreCliente")
            facturas_fechaCompra = miForm.cleaned_data.get("fechaCompra")
            facturas = Facturas(nombreProducto=facturas_nombreProducto, nombreVendedor=facturas_nombreVendedor, nombreCliente=facturas_nombreCliente, fechaCompra=facturas_fechaCompra)
            facturas.save()
            
            contexto = {'facturas': Facturas.objects.all()}
            return render(request, "aplicacion/facturas.html", contexto)
    else:
        miForm = FacturasForm()
        
    return render(request, "aplicacion/facturasForm.html", {"form": miForm})

def buscarProductos(request):
    return render(request, "aplicacion/index.html")

def encontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Productos.objects.filter(nombre__icontains=patron)
        contexto =  {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    
    contexto = {'productos': Productos.objects.all()}
    return render(request, "aplicacion/productos.html", contexto)