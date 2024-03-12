from django import forms

class VendedoresForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    correo = forms.EmailField(required=True)
    fechaInicio = forms.DateField(required=True)
    venta = forms.FloatField(required=True)

class ClientesForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    correo = forms.EmailField(required=True)
    fechaInicio = forms.DateField(required=True)
    compra = forms.FloatField(required=True)

class ProductosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    vendedor = forms.CharField(max_length=50, required=True)
    fechaRegistro = forms.DateField(required=True)
    costo = forms.FloatField(required=True)

class FacturasForm(forms.Form):
    nombreProducto = forms.CharField(max_length=50, required=True)
    nombreVendedor = forms.CharField(max_length=50, required=True)
    nombreCliente = forms.CharField(max_length=50, required=True)
    fechaCompra = forms.DateField(required=True)