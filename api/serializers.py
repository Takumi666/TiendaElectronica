from rest_framework import serializers
from sistema.models import Producto,Sucursal,Vendedor,Venta,Oferta

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

class OfertasSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("__all__")
		model = Oferta
