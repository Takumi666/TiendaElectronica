from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sistema.models import Producto,Sucursal,Vendedor,Venta
from .serializers import ProductoSerializer

# Create your views here.
class VistaProducto(APIView):
	def get(self, request):
		productos = Producto.objects.all()
		serializer = ProductoSerializer(productos, many = True)
		return Response(serializer.data)

class VistaSucursal(APIView):
	def get(self, request):
		sucursales = Sucursal.objects.all()
		serializer = ProductoSerializer(sucursales, many = True)
		return Response(serializer.data)

class VistaVendedor(APIView):
	def get(self, request):
		vendedores = Vendedor.objects.all()
		serializer = ProductoSerializer(vendedores, many = True)
		return Response(serializer.data)

class VistaVenta(APIView):
	def get(self, request):
		ventas = Venta.objects.all()
		serializer = ProductoSerializer(ventas, many = True)
		return Response(serializer.data)
