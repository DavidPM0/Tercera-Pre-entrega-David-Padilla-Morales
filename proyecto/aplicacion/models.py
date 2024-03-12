from django.db import models

# Create your models here.

class Vendedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    fechaInicio = models.DateField()
    venta = models.FloatField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    fechaInicio = models.DateField()
    compra = models.FloatField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=50)
    fechaRegistro = models.DateField()
    costo = models.FloatField()

    def __str__(self):
        return f"{self.nombre}"

class Facturas(models.Model):
    nombreProducto = models.CharField(max_length=50)
    nombreVendedor = models.CharField(max_length=50)
    nombreCliente = models.CharField(max_length=50)
    fechaCompra = models.DateField()

    def __str__(self):
        return f"{self.nombreProducto}"