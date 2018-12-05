from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sistema.models import Producto,Sucursal,Vendedor,Venta,Oferta
from .serializers import ProductoSerializer,VentaSerializer,VendedorSerializer,SucursalSerializer,OfertasSerializer

# Create your views here.
class VistaProducto(APIView):
	def get(self, request):
		productos = Producto.objects.all()
		serializer = ProductoSerializer(productos, many = True)
		return Response(serializer.data)

class VistaSucursal(APIView):
	def get(self, request):
		sucursales = Sucursal.objects.all()
		serializer = SucursalSerializer(sucursales, many = True)
		return Response(serializer.data)

class VistaVendedor(APIView):
	def get(self, request):
		vendedores = Vendedor.objects.all()
		serializer = VendedorSerializer(vendedores, many = True)
		return Response(serializer.data)

class VistaVenta(APIView):
	def get(self, request):
		ventas = Venta.objects.all()
		serializer = VentaSerializer(ventas, many = True)
		return Response(serializer.data)

class VistaOferta(APIView):
	def get(self, request):
		oferta = Oferta.objects.all()
		serializer = OfertasSerializer(oferta, many = True)
		return Response(serializer.data)
