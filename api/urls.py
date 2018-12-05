from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^productos$", views.VistaProducto.as_view()),
	url(r"^sucursales$", views.VistaSucursal.as_view()),
	url(r"^vendedores$", views.VistaVendedor.as_view()),
	url(r"^ventas$", views.VistaVenta.as_view()),
	url(r"^ofertas$", views.VistaOferta.as_view()),
]
