from rest_framework import serializers
from sistema.models import Producto

# Serializers
class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ("__all__")
		model = Producto
