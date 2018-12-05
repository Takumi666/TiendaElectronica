from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
	url(r"^$", views.index, name = "index"),
	url(r"^cuentas/login$", views.iniciar_sesion, name = "login"),
	url(r"^cuentas/logout$", views.cerrar_sesion, name = "logout"),
	url(r"^cuentas/recuperarpass/$", views.recuperar_password, name = "recuperarPassword"),
	url(r"^cuentas/cambiarpass/(?P<token>[\w\.-]+)&(?P<user>[\w\.]+)$", views.cambiar_password, name = "cambiarPassword"),
	url(r"^Catalogo$", views.tienda, name = "Tienda"),
	url(r"^Ofertas$", views.ofertas, name = "Ofertas"),
	url(r"^gestion$", views.menu_gestion, name = "menu_gestion"),

	# Ventas
	url(r"^ventas$", views.modulo_ventas, name = "modulo_ventas"),
	url(r"^ventas/registrar$" ,views.registrar_venta, name = "registrar_venta"),
	url(r"^ventas/(?P<pk>[0-9]+)$", views.ver_venta, name = "ver_venta"),
	url(r"^ventas/actualizar/(?P<pk>[0-9]+)$", views.actualizar_venta, name = "actualizar_venta"),
	url(r"^ventas/anular/(?P<pk>[0-9]+)$", views.anular_venta, name = "anular_venta"),

	# Productos
	url(r"^gestion/productos$", views.gestion_productos, name = "gestion_productos"),
	url(r"^gestion/productos/registrar$", views.registrar_producto, name = "registrar_producto"),
	url(r"^gestion/productos/(?P<pk>[0-9]+)$", views.ver_producto, name = "ver_producto"),
	url(r"^gestion/productos/actualizar/(?P<pk>[0-9]+)$", views.actualizar_producto, name = "actualizar_producto"),
	url(r"^gestion/productos/eliminar/(?P<pk>[0-9]+)$", views.eliminar_producto, name = "eliminar_producto"),

	# Sucursales
	url(r"^gestion/sucursales$", views.gestion_sucursales, name = "gestion_sucursales"),
	url(r"^gestion/sucursales/registrar$", views.registrar_sucursal, name = "registrar_sucursal"),
	url(r"^gestion/sucursales/(?P<pk>[0-9]+)$", views.ver_sucursal, name = "ver_sucursal"),
	url(r"^gestion/sucursales/actualizar/(?P<pk>[0-9]+)$", views.actualizar_sucursal, name = "actualizar_sucursal"),
	url(r"^gestion/sucursales/eliminar/(?P<pk>[0-9]+)$", views.eliminar_sucursal, name = "eliminar_sucursal"),

	# Vendedores
	url(r"^gestion/vendedores$", views.gestion_vendedores, name = "gestion_vendedores"),
	url(r"^gestion/vendedores/registrar$", views.registrar_vendedor, name = "registrar_vendedor"),
	url(r"^gestion/vendedores/(?P<pk>[0-9]+)$", views.ver_vendedor, name = "ver_vendedor"),
	url(r"^gestion/vendedores/actualizar/(?P<pk>[0-9]+)$", views.actualizar_vendedor, name = "actualizar_vendedor"),
	url(r"^gestion/vendedores/eliminar/(?P<pk>[0-9]+)$", views.eliminar_vendedor, name = "eliminar_vendedor"),

	# Ofertas
	url(r"^gestion/ofertas$", views.gestion_ofertas, name = "gestion_ofertas"),
	url(r"^gestion/ofertas/registrar$", views.registrar_oferta, name = "registrar_oferta"),
	url(r"^gestion/ofertas/(?P<pk>[0-9]+)$", views.ver_oferta, name = "ver_oferta"),
	url(r"^gestion/ofertas/actualizar/(?P<pk>[0-9]+)$", views.actualizar_oferta, name = "actualizar_oferta"),
	url(r"^gestion/ofertas/eliminar/(?P<pk>[0-9]+)$", views.eliminar_oferta, name = "eliminar_oferta"),

	#Worker
	path(r'base_layout/',views.base_layout,name='base_layout'),
]
