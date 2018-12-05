from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from sistema.forms import ProductoForm, VendedorForm, SucursalForm, VentaForm, LoginForm
from sistema.models import Producto, Vendedor, Sucursal, Venta

# Create your views here.
def index(request):
	return render(request, "index.html", { "titulo": "Inicio" }) # Retorna la vista solicitada

# Inicio de sesión
def iniciar_sesion(request):
	if request.user.is_authenticated: # Verifica si el usuario tiene la sesión abierta
		return redirect("index") # En caso de que sea verdadero redirecciona a la página principal

	login_fail = False # Estado que determina el error de inicio de sesión
	if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
		form = LoginForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
		if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
			data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
			user = authenticate(username = data.get("username"), password = data.get("password")) # Proceso de autenticación de credenciales
			if user: # Verifica si el usuario es válido
				login(request, user) # En caso de que sea válido se abre una sesión para dicho usuario ingresado
				return redirect("index") # Redirecciona a la página principal
			login_fail = True # Si no son válidas las credenciales, este estado pasa a ser verdadero
	form = LoginForm() # Se instancia el formulario
	return render(request, "login.html", { "titulo": "Iniciar sesión", "form": form, "login_fail": login_fail }) # Retorna la vista solicitada

# Cierre de sesión
def cerrar_sesion(request):
	if request.user.is_authenticated: # Verifica si el usuario tiene la sesión abierta
		logout(request) # Se cierra la sesión del usuario
	return redirect("index") # Redirecciona a la página principal

@login_required
@staff_member_required
def menu_gestion(request):
	return render(request, "gestion/inicio.html", { "titulo": "Menú gestión" })

"""
Gestión de productos
"""
@login_required
@staff_member_required
def gestion_productos(request):
	return render(request, "gestion/gestionProductos.html", { "titulo": "Gestión de productos" })

@login_required
@staff_member_required
def registrar_producto(request):
	if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
		form = ProductoForm(request.POST, request.FILES) # Se instancia el formulario pasando como parámetro los datos ingresados
		if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
			data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
			Producto.objects.create(nombre = data.get("nombre"), descripcion = data.get("descripcion"), precio = data.get("precio"), tipo = data.get("tipo"), foto = data.get("foto")) # Se añade un nuevo registro de producto a la base de datos
			return redirect("gestion_productos") # Redirecciona al menú de gestión de productos
	else: # Se asume que la vista fue solicitada sin envío de formulario
		form = ProductoForm() # Se instancia un nuevo formulario para ingresar datos del nuevo registro
	return render(request, "gestion/registrarProducto.html", { "titulo": "Registrar un producto", "form": form }) # Retorna la vista solicitada

def ver_producto(request, pk):
	try:
		producto = Producto.objects.get(codigo = pk) # Obtiene el producto solicitado con el identificador que se pasa como parámetro
	except ObjectDoesNotExist: # Esta excepción cubre el error cuando el registro de un producto no existe
		producto = None # Cuando no exista el producto, se asigna como valor nulo a esta variable
	return render(request, "verProducto.html", { "producto": producto }) # Retorna la vista solicitada

@login_required
@staff_member_required
def actualizar_producto(request, pk):
	try:
		producto = Producto.objects.get(codigo = pk) # Obtiene el producto solicitado con el identificador que se pasa como parámetro
		if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
			form = ProductoForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
			if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
				data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
				# Se procede la actualización de los datos del producto solicitado
				producto.nombre = data.get("nombre")
				producto.descripcion = data.get("descripcion")
				producto.precio = data.get("precio")
				if request.FILES.get("foto"):
					producto.foto = request.FILES["foto"]
				producto.save() # Se guardan los cambios realizados
				return redirect("gestion_productos") # Redirecciona al menú de gestión de productos
		else: # Se asume que la vista fue solicitada sin envío de formulario
			form = ProductoForm({ "nombre": producto.nombre, "descripcion": producto.descripcion, "precio": producto.precio, "foto": producto.foto }) # Se instancia el formulario con los valores del registro a modificar
	except ObjectDoesNotExist: # En caso de que el registro no exista se asignan en nulo las variables producto y form
		producto = None
		form = None
	return render(request, "gestion/actualizarProducto.html", { "titulo": "Actualizar producto", "form": form, "producto": producto}) # Retorna la vista solicitada

@login_required
@staff_member_required
def eliminar_producto(request, pk):
	try:
		producto = Producto.objects.get(codigo = pk) # Obtiene el producto solicitado con el identificador que se pasa como parámetro
		if producto: # Verifica que el producto existe
			producto.delete() # Se elimina el producto solicitado
		return redirect("gestion_productos") # Redirecciona al menú de gestión de productos
	except ObjectDoesNotExist: # En caso de algún error se procede a mostrar la página describiendo lo ocurrido
		return render(request, "gestion/eliminarProductoError.html", { "titulo": "Error al eliminar producto" }) # Retorna la vista con el error generado

"""
Gestión de vendedores
"""
@login_required
@staff_member_required
def gestion_vendedores(request):
	return render(request, "gestion/gestionVendedores.html", { "titulo": "Gestión de vendedores"})

@login_required
@staff_member_required
def registrar_vendedor(request):
	if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
		form = VendedorForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
		if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
			data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
			user = User.objects.create_user(username = (data.get("nombres")[:2] + "." + data.get("apPaterno")).lower(), password = data.get("run")) # Se crea un usuario que se va a asociar con el vendedor
			Vendedor.objects.create(usuario = user, run = data.get("run"), nombres = data.get("nombres"), apPaterno = data.get("apPaterno"), apMaterno = data.get("apMaterno"), sucursal = data.get("sucursal")) # Se crea un registro del vendedor
			return redirect("gestion_vendedores") # Redirecciona al menú de gestión de vendedores
	else: # Se asume que la vista fue solicitada sin envío de formulario
		form = VendedorForm() # Se instancia un nuevo formulario para ingresar datos del nuevo registro
	return render(request, "gestion/registrarVendedor.html", { "titulo": "Registrar un vendedor", "form": form })

@login_required
@staff_member_required
def ver_vendedor(request, pk):
	try:
		vendedor = Vendedor.objects.get(codigo = pk) # Obtiene el vendedor solicitado con el identificador que se pasa como parámetro
	except ObjectDoesNotExist: # Esta excepción cubre el error cuando el registro de un vendedor no existe
		vendedor = None # Cuando no exista el vendedor, se asigna como valor nulo a esta variable
	return render(request, "gestion/verVendedor.html", { "vendedor": vendedor }) # Retorna la vista solicitada

@login_required
@staff_member_required
def actualizar_vendedor(request, pk):
	try:
		vendedor = Vendedor.objects.get(codigo = pk) # Obtiene el vendedor solicitado con el identificador que se pasa como parámetro
		if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
			form = VendedorForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
			if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
				data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
				# Se procede la actualización de los datos del vendedor solicitado
				vendedor.run = data.get("run")
				vendedor.nombres = data.get("nombres")
				vendedor.apPaterno = data.get("apPaterno")
				vendedor.apMaterno = data.get("apMaterno")
				vendedor.sucursal = data.get("sucursal")
				vendedor.save() # Se guardan los cambios realizados
				return redirect("gestion_vendedores") # Redirecciona al menú de gestión de vendedores
		else: # Se asume que la vista fue solicitada sin envío de formulario
			form = VendedorForm({ "run": vendedor.run, "nombres": vendedor.nombres, "apPaterno": vendedor.apPaterno, "apMaterno": vendedor.apMaterno, "sucursal": vendedor.sucursal }) # Se instancia el formulario con los valores del registro a modificar
	except ObjectDoesNotExist:  # En caso de que el registro no exista se asignan en nulo las variables vendedor y form
		vendedor = None
		form = None
	return render(request, "gestion/actualizarVendedor.html", { "titulo": "Actualizar vendedor", "form": form, "vendedor": vendedor }) # Retorna la vista solicitada

@login_required
@staff_member_required
def eliminar_vendedor(request, pk):
	try:
		vendedor = Vendedor.objects.get(codigo = pk) # Obtiene el vendedor solicitado con el identificador que se pasa como parámetro
		if vendedor: # Verifica que el vendedor existe
			vendedor.usuario.delete() # Se elimina el usuario asociado al vendedor
			vendedor.delete() # Se elimina el vendedor solicitado
		return redirect("gestion_vendedores") # Redirecciona al menú de gestión de vendedores
	except ObjectDoesNotExist: # En caso de algún error se procede a mostrar la página describiendo lo ocurrido
		return render(request, "gestion/eliminarVendedorFail.html", { "titulo": "Error al eliminar vendedor" }) # Retorna la vista con el error generado

"""
Gestión de sucursales
"""
@login_required
@staff_member_required
def gestion_sucursales(request):
	return render(request, "gestion/gestionSucursales.html", { "titulo": "Gestión de sucursales" })

@login_required
@staff_member_required
def registrar_sucursal(request):
	if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
		form = SucursalForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
		if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
			data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
			Sucursal.objects.create(nombre = data.get("nombre"), ciudad = data.get("ciudad"), comuna = data.get("comuna"), direccion = data.get("direccion"), telefono = data.get("telefono"), correo = data.get("correo")) # Se crea un registro de la sucursal
			return redirect("gestion_sucursales") # Redirecciona al menú de gestión de productos
	else: # Se asume que la vista fue solicitada sin envío de formulario
		form = SucursalForm() # Se instancia un nuevo formulario para ingresar datos del nuevo registro
	return render(request, "gestion/registrarSucursal.html", { "titulo": "Registrar una sucursal", "form": form })

@login_required
@staff_member_required
def ver_sucursal(request, pk):
	try:
		sucursal = Sucursal.objects.get(codigo = pk) # Obtiene la sucursal solicitada con el identificador que se pasa como parámetro
	except ObjectDoesNotExist: # Esta excepción cubre el error cuando el registro de una sucursal no existe
		sucursal = None # Cuando no exista la sucursal, se asigna como valor nulo a esta variable
	return render(request, "gestion/verSucursal.html", { "sucursal": sucursal }) # Retorna la vista solicitada

@login_required
@staff_member_required
def actualizar_sucursal(request, pk):
	try:
		sucursal = Sucursal.objects.get(codigo = pk) # Obtiene la sucursal solicitada con el identificador que se pasa como parámetro
		if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
			form = SucursalForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
			if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
				data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
				# Se procede la actualización de los datos de la sucursal solicitada
				sucursal.nombre = data.get("nombre")
				sucursal.ciudad = data.get("ciudad")
				sucursal.comuna = data.get("comuna")
				sucursal.direccion = data.get("direccion")
				sucursal.telefono = data.get("telefono")
				sucursal.correo = data.get("correo")
				sucursal.save() # Se guardan los cambios realizados
				return redirect("gestion_sucursales") # Redirecciona al menú de gestión de sucursales
		else: # Se asume que la vista fue solicitada sin envío de formulario
			form = SucursalForm({ "nombre": sucursal.nombre, "ciudad": sucursal.ciudad, "comuna": sucursal.comuna, "direccion": sucursal.direccion, "telefono": sucursal.telefono, "correo": sucursal.correo }) # Se instancia el formulario con los valores del registro a modificar
	except ObjectDoesNotExist:  # En caso de que el registro no exista se asignan en nulo las variables sucursal y form
		sucursal = None
		form = None
	return render(request, "gestion/actualizarSucursal.html", { "titulo": "Actualizar sucursal", "form": form, "sucursal": sucursal }) # Retorna la vista solicitada

@login_required
@staff_member_required
def eliminar_sucursal(request, pk):
	try:
		sucursal = Sucursal.objects.get(codigo = pk) # Obtiene la sucursal solicitada con el identificador que se pasa como parámetro
		if sucursal: # Verifica que la sucursal existe
			producto.delete() # Se elimina la sucursal solicitada
		return redirect("gestion_sucursales") # Redirecciona al menú de gestión de sucursales
	except ObjectDoesNotExist: # En caso de algún error se procede a mostrar la página describiendo lo ocurrido
		return render(request, "gestion/eliminarSucursalError.html", { "titulo": "Error al eliminar sucursal" }) # Retorna la vista con el error generado

"""
Módulo de ventas
"""
@login_required
def modulo_ventas(request):
	return render(request, "ventas/inicio.html", { "titulo": "Módulo de ventas" })

@login_required
def registrar_venta(request):
	if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
		form = VentaForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
		vendedor = Vendedor.objects.get(usuario = request.user)
		if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
			data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
			Venta.objects.create(vendedor = vendedor, sucursal = vendedor.sucursal, producto = data.get("producto"), cantidad = data.get("cantidad"), comentario = data.get("comentario")) # Se registra una nueva venta
			return redirect("modulo_ventas") # Redirecciona al menú de gestión de vendedores
	else: # Se asume que la vista fue solicitada sin envío de formulario
		form = VentaForm() # Se instancia un nuevo formulario para ingresar datos del nuevo registro
	return render(request, "ventas/registrarVenta.html", { "titulo": "Registrar una venta", "form": form }) # Retorna la vista solicitada

@login_required
def ver_venta(request, pk):
	try:
		venta = Venta.objects.get(codigo = pk) # Obtiene la venta solicitada con el identificador que se pasa como parámetro
	except: # Esta excepción cubre el error cuando el registro de una venta no existe
		venta = None # Cuando no exista la venta, se asigna como valor nulo a esta variable
	return redirect(request, "ventas/verVenta.html", { "venta": venta }) # Retorna la vista solicitada

@login_required
def actualizar_venta(request, pk):
	try:
		venta = Venta.objects.get(codigo = pk) # Obtiene la venta solicitada con el identificador que se pasa como parámetro
		if request.method == "POST": # Verifica si la solicitud de esta vista lleva consigo el envío de formulario
			form = VentaForm(request.POST) # Se instancia el formulario pasando como parámetro los datos ingresados
			if form.is_valid(): # Inicia el proceso de validación y verifica si los datos ingresados esten correctos
				data = form.cleaned_data # Extrae los datos ingresados del formulario a esta variable
				# Se procede la actualización de los datos de la venta solicitada
				venta.producto = data.get("producto")
				venta.cantidad = data.get("cantidad")
				venta.comentario = data.get("comentario")
				venta.save() # Se guardan los cambios realizados
				return redirect("modulo_ventas") # Redirecciona al módulo de ventas
		else: # Se asume que la vista fue solicitada sin envío de formulario
			form = VentaForm({ "producto": venta.producto, "cantidad": venta.cantidad, "comentario": venta.comentario }) # Se instancia el formulario con los valores del registro a modificar
	except ObjectDoesNotExist: # En caso de que el registro no exista se asignan en nulo las variables venta y form
		venta = None
		form = None
	return render(request, "ventas/actualizarVenta.html", { "titulo": "Actualizar venta", "form": form, "venta": venta }) # Retorna la vista solicitada

@login_required
def anular_venta(request, pk):
	try:
		venta = Venta.objects.get(codigo = pk) # Obtiene la venta solicitada con el identificador que se pasa como parámetro
		if venta: # Verifica que la venta existe
			venta.anulada = True # Se anula la venta solicitada
			venta.save() # Guarda los cambios
		return redirect("modulo_ventas") # Redirecciona al módulo de ventas
	except ObjectDoesNotExist: # En caso de algún error se procede a mostrar la página describiendo lo ocurrido
		return render(request, "gestion/anularVentaError.html", { "titulo": "Error al anular venta" }) # Retorna la vista con el error generado
