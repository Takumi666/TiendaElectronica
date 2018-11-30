from django.db import models

# Create your models here.
class Sucursal(models.Model):
	codigo = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	direccion = models.CharField(max_length = 50)
	ciudad = models.CharField(max_length = 30)
	comuna = models.CharField(max_length = 30)
	telefono = models.IntegerField()
	correo = models.EmailField()
	encargado = models.CharField()

class Vendedor(models.Model):
	codigo = models.AutoField(primary_key = True)
	nombres = models.CharField(max_length = 30)
	apPaterno = models.CharField(max_length = 20)
	apMaterno = models.CharField(max_length = 20)
	sucursal = models.ForeignKey(Sucursal, on_delete = models.DO_NOTHING)

class Producto(models.Model):
	codigo = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 50)
	descripcion = models.TextField()
	precio = models.IntegerField()
	tipo = models.CharField(max_length = 20)

class Venta(models.Model):
	codigo = models.AutoField(primary_key = True)
	fechaHora = models.DateTimeField()
	cantidad = models.IntegerField()
	sucursal = models.ForeignKey(Sucursal, on_delete = models.DO_NOTHING)
	comentario = models.TextField(null = True)
