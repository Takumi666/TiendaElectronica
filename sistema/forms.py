from django import forms
from .models import Producto, Sucursal, Oferta

CIUDADES = (
	("Santiago", "Santiago"),
)
VIGENTE = (
	("True", "True"),
	("False", "False"),
)
COMUNAS = (
	("Ñuñoa", "Ñuñoa"),
	("Providencia", "Providencia"),
)
TIPOS = (
	("Procesadores", "Procesadores"),
	("Accesorios", "Accesorios"),
	("RAM", "RAM"),
	("Tarjeta de Video", "Tarjeta de Video"),
)

# Formularios
class VentaForm(forms.Form):
	producto = forms.ModelChoiceField(label = "Producto", queryset = Producto.objects.all(), widget = forms.Select(attrs = { "id": "producto", "class": "campo" }))
	cantidad = forms.IntegerField(label = "Cantidad", widget = forms.NumberInput(attrs = { "id": "cantidad", "class": "campo", "min": "0" }))
	comentario = forms.CharField(label = "Comentario", required = False, widget = forms.Textarea(attrs = { "id": "comentario", "class": "campo", "placeholder": "Ingrese comentario de la venta" }))

class ProductoForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "class": "campo", "placeholder": "Ingrese nombre del producto"}))
	descripcion = forms.CharField(label = "Descripción", widget = forms.Textarea(attrs = { "id": "descripcion", "class": "campo", "placeholder": "Ingrese descripción del producto" }))
	precio = forms.IntegerField(label = "Precio", widget = forms.NumberInput(attrs = { "id": "precio", "class": "campo", "min": "0" }))
	tipo = forms.ChoiceField(label = "Tipo de producto", choices = TIPOS, widget = forms.Select(attrs = { "id": "tipo", "class": "campo" }))
	foto = forms.ImageField(label = "Foto", required = False, widget = forms.ClearableFileInput(attrs = { "id": "foto" }))

class VendedorForm(forms.Form):
	run = forms.CharField(label = "RUN", widget = forms.TextInput(attrs = { "id": "run", "class": "campo", "placeholder": "12345678-9" }))
	nombres = forms.CharField(label = "Nombres", widget = forms.TextInput(attrs = { "id": "nombres", "class": "campo", "placeholder": "Juan Armando" }))
	apPaterno = forms.CharField(label = "Apellido paterno", widget = forms.TextInput(attrs = { "id": "appaterno", "class": "campo", "placeholder": "Pérez" }))
	apMaterno = forms.CharField(label = "Apellido materno", widget = forms.TextInput(attrs = { "id": "apmaterno", "class": "campo", "placeholder": "Cisternas" }))
	sucursal = forms.ModelChoiceField(label = "Sucursal", empty_label = None, queryset = Sucursal.objects.all(), widget = forms.Select(attrs = { "id": "sucursal", "class": "campo" }))

class SucursalForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "class": "campo", "placeholder": "Sucursal Lyon"}))
	ciudad = forms.ChoiceField(label = "Ciudad", choices = CIUDADES, widget = forms.Select(attrs = { "id": "ciudad", "class": "campo" }))
	comuna = forms.ChoiceField(label = "Comuna", choices = COMUNAS, widget = forms.Select(attrs = { "id": "comuna", "class": "campo" }))
	direccion = forms.CharField(label = "Dirección", widget = forms.TextInput(attrs = { "id": "direccion", "class": "campo", "placeholder": "Av. Suecia #123"}))
	telefono = forms.IntegerField(label = "Teléfono", widget = forms.TextInput(attrs = { "id": "telefono", "class": "campo", "placeholder": "123456789"}))
	correo = forms.EmailField(label = "Correo electrónico", widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "direccion@correo.com" }))

class LoginForm(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", widget = forms.TextInput(attrs = { "id": "username", "class": "campo", "placeholder": "Ingrese nombre de usuario" }))
	password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs = { "id": "password", "class": "campo", "placeholder": "Ingrese contraseña" }))

class OfertaForm(forms.Form):
	fechaFin = forms.DateField(label = "Fecha fin", widget = forms.DateInput(attrs = { "id": "fecha-fin", "class": "campo" }))
	porcentaje = forms.DecimalField(label = "Porcentaje de descuento", widget = forms.NumberInput(attrs = { "id": "porcentaje", "class": "campo" }))
	producto = forms.ModelChoiceField(label = "Producto", queryset = Producto.objects.all(), widget = forms.Select(attrs = { "id": "producto", "class": "campo" }))
	sucursal = forms.ModelChoiceField(label = "Sucursal", queryset = Sucursal.objects.all(), widget = forms.Select(attrs = { "id": "sucursal", "class": "campo" }))
	vigente = forms.ChoiceField(label = "Vigente", choices = VIGENTE, widget = forms.Select(attrs = { "id": "vigente", "class": "campo" }))

# Formulario de recuperación de contraseña
class FormRecuperarPassword(forms.Form):
	correo = forms.EmailField(label = "Correo electrónico", max_length = 30, widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "Ingrese correo" }))

# Formulario de cambio de contraseña
class FormCambioPassword(forms.Form):
	nuevaPassword = forms.CharField(label = "Nueva contraseña", widget = forms.PasswordInput(attrs = { "id": "nuevapass", "class": "campo", "placeholder": "Ingrese nueva contraseña" }))
	confirmPassword = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput(attrs = { "id": "confirmpass", "class": "campo", "placeholder": "Confirme nueva contraseña" }))
