from rest_framework import serializers
from sistema.models import Producto,Sucursal,Vendedor,Venta

# Serializers
class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("__all__")
		model = Producto

class SucursalSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("__all__")
		model = Sucursal

class VendedorSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("__all__")
		model = Vendedor

class VentaSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("__all__")
		model = Venta
