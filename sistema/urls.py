from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name = "index"),
	url(r"^cuentas/login$", views.iniciar_sesion, name = "login"),
	url(r"^cuentas/logout$", views.cerrar_sesion, name = "logout"),
	url(r"^gestion/productos$", views.gestion_productos, name = "gestion_productos"),
	url(r"^gestion/productos/registrar$", views.registrar_producto, name = "registrar_producto"),
	url(r"^gestion/productos/(?P<pk>[0-9]+)$", views.ver_producto, name = "ver_producto"),
	url(r"^gestion/productos/actualizar/(?P<pk>[0-9]+)$", views.actualizar_producto, name = "actualizar_producto"),
	url(r"^gestion/productos/eliminar/(?P<pk>[0-9]+)$", views.eliminar_producto, name = "eliminar_producto"),
]
