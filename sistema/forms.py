from django import forms
from .models import Producto

REGIONES = []
COMUNAS = []
TIPO = ["Computación",]

# Formularios
class ProductoForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Ingrese nombre del producto"}))
	descripcion = forms.CharField(label = "Descripción", widget = forms.Textarea(attrs = { "id": "descripcion", "placeholder": "Ingrese descripción del producto" }))
	precio = forms.IntegerField(label = "Precio", widget = forms.NumberInput(attrs = { "id": "precio" }))
	tipo = forms.ChoiceField(label = "Tipo de producto", choices = TIPO, widget = forms.Select(attrs = { "id": "tipo" }))
	foto = forms.ImageField(label = "Foto", required = False, widget = forms.ClearableFileInput(attrs = { "id": "foto" }))

class LoginForm(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", widget = forms.TextInput(attrs = { "id": "username", "placeholder": "Ingrese nombre de usuario" }))
	password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs = { "id": "password", "placeholder": "Ingrese contraseña" }))
