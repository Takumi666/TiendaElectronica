from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from sistema.forms import ProductoForm, LoginForm
from sistema.models import Producto

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

"""
Gestión de productos
"""
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
				return redirect("gestionProductos") # Redirecciona al menú de gestión de productos
		form = ProductoForm({ "nombre": producto.nombre, "descripcion": producto.descripcion, "precio": producto.precio, "foto": producto.foto })
	except ObjectDoesNotExist:
		producto = None

@login_required
@staff_member_required
def eliminar_producto(request, pk):
	try:
		producto = Producto.objects.get(codigo = pk) # Obtiene el producto solicitado con el identificador que se pasa como parámetro
		if producto: # Verifica que el producto existe
			producto.delete() # Se elimina el producto solicitado
		return redirect("gestionProductos") # Redirecciona al menú de gestión de productos
	except ObjectDoesNotExist: # En caso de algún error se procede a mostrar la página describiendo lo ocurrido
		return render(request, "eliminarProductoError.html", { "titulo": "Error al eliminar producto" }) # Retorna la vista con el error generado
