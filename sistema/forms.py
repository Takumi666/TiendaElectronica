from django import forms
from .models import Producto

CIUDADES = []
COMUNAS = []
TIPOS = [ "Procesadores", ]

# Formularios
class ProductoForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Ingrese nombre del producto"}))
	descripcion = forms.CharField(label = "Descripción", widget = forms.Textarea(attrs = { "id": "descripcion", "placeholder": "Ingrese descripción del producto" }))
	precio = forms.IntegerField(label = "Precio", widget = forms.NumberInput(attrs = { "id": "precio" }))
	tipo = forms.ChoiceField(label = "Tipo de producto", choices = TIPOS, widget = forms.Select(attrs = { "id": "tipo" }))
	foto = forms.ImageField(label = "Foto", required = False, widget = forms.ClearableFileInput(attrs = { "id": "foto" }))

class TiendaForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Ingrese nombre de la tienda"}))
	ciudad = forms.ChoiceField(label = "Ciudad", choices = CIUDADES, widget = forms.Select(attrs = { "id": "ciudad" }))
	comuna = forms.ChoiceField(label = "Comuna", choices = COMUNAS, widget = forms.Select(attrs = { "id": "comuna" }))
	direccion = forms.CharField(label = "Dirección", widget = forms.TextInput(attrs = { "id": "direccion", "placeholder": "Calle Falsa #123"}))
	telefono = forms.IntegerField(label = "Teléfono", widget = forms.TextInput(attrs = { "id": "telefono", "placeholder": "123456789"}))
	correo = forms.EmailField(label = "Correo electrónico", widget = forms.EmailInput(attrs = { "id": "correo", "placeholder": "direccion@correo.com" }))

class LoginForm(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", widget = forms.TextInput(attrs = { "id": "username", "placeholder": "Ingrese nombre de usuario" }))
	password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs = { "id": "password", "placeholder": "Ingrese contraseña" }))
