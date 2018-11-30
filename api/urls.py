from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^productos$", views.VistaProducto.as_view()),
]
