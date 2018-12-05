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
	producto = forms.ModelChoiceField(label = "Producto", queryset = Producto.objects.all(), widget = forms.Select(attrs = { "id": "producto" }))
	cantidad = forms.IntegerField(label = "Cantidad", widget = forms.NumberInput(attrs = { "id": "cantidad" }))
	comentario = forms.CharField(label = "Comentario", required = False, widget = forms.Textarea(attrs = { "id": "comentario", "placeholder": "Ingrese comentario de la venta" }))



class ProductoForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Ingrese nombre del producto"}))
	descripcion = forms.CharField(label = "Descripción", widget = forms.Textarea(attrs = { "id": "descripcion", "placeholder": "Ingrese descripción del producto" }))
	precio = forms.IntegerField(label = "Precio", widget = forms.NumberInput(attrs = { "id": "precio" }))
	tipo = forms.ChoiceField(label = "Tipo de producto", choices = TIPOS, widget = forms.Select(attrs = { "id": "tipo" }))
	foto = forms.ImageField(label = "Foto", required = False, widget = forms.ClearableFileInput(attrs = { "id": "foto" }))

class VendedorForm(forms.Form):
	run = forms.CharField(label = "RUN", widget = forms.TextInput(attrs = { "id": "run", "placeholder": "12345678-9" }))
	nombres = forms.CharField(label = "Nombres", widget = forms.TextInput(attrs = { "id": "nombres", "placeholder": "Juan Armando" }))
	apPaterno = forms.CharField(label = "Apellido paterno", widget = forms.TextInput(attrs = { "id": "appaterno", "placeholder": "Pérez" }))
	apMaterno = forms.CharField(label = "Apellido materno", widget = forms.TextInput(attrs = { "id": "apmaterno", "placeholder": "Cisternas" }))
	sucursal = forms.ModelChoiceField(label = "Sucursal", queryset = Sucursal.objects.all(), widget = forms.Select(attrs = { "id": "sucursal" }))

class SucursalForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Santa Isabel"}))
	ciudad = forms.ChoiceField(label = "Ciudad", choices = CIUDADES, widget = forms.Select(attrs = { "id": "ciudad" }))
	comuna = forms.ChoiceField(label = "Comuna", choices = COMUNAS, widget = forms.Select(attrs = { "id": "comuna" }))
	direccion = forms.CharField(label = "Dirección", widget = forms.TextInput(attrs = { "id": "direccion", "placeholder": "Calle Falsa #123"}))
	telefono = forms.IntegerField(label = "Teléfono", widget = forms.TextInput(attrs = { "id": "telefono", "placeholder": "123456789"}))
	correo = forms.EmailField(label = "Correo electrónico", widget = forms.EmailInput(attrs = { "id": "correo", "placeholder": "direccion@correo.com" }))

class LoginForm(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", widget = forms.TextInput(attrs = { "id": "username", "placeholder": "Ingrese nombre de usuario" }))
	password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs = { "id": "password", "placeholder": "Ingrese contraseña" }))

class OfertaForm(forms.Form):
	fechaFin = forms.DateField(label = "Fecha fin", widget = forms.DateInput(attrs = { "id": "fecha-fin" }))
	fechaInicio = forms.DateField(label = "Fecha Inicio", widget = forms.DateInput(attrs = { "id": "fecha-inicio" }))
	porcentaje = forms.DecimalField(label = "Porcentaje de descuento", widget = forms.NumberInput(attrs = { "id": "porcentaje" }))
	producto = forms.ModelChoiceField(label = "Producto", queryset = Producto.objects.all(), widget = forms.Select(attrs = { "id": "producto" }))
	sucursal = forms.ModelChoiceField(label = "Sucursal", queryset = Sucursal.objects.all(), widget = forms.Select(attrs = { "id": "sucursal" }))
	vigente = forms.ChoiceField(label = "Vigente", choices = VIGENTE, widget = forms.Select(attrs = { "vignete": "vigente" }))

# Formulario de recuperación de contraseña
class FormRecuperarPassword(forms.Form):
	correo = forms.EmailField(label = "Correo electrónico", max_length = 30, widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "Ingrese correo" }))

# Formulario de cambio de contraseña
class FormCambioPassword(forms.Form):
	nuevaPassword = forms.CharField(label = "Nueva contraseña", widget = forms.PasswordInput(attrs = { "id": "nuevapass", "class": "campo", "placeholder": "Ingrese nueva contraseña" }))
	confirmPassword = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput(attrs = { "id": "confirmpass", "class": "campo", "placeholder": "Confirme nueva contraseña" }))
