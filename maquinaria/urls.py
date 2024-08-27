from django.urls import path
from . import views

urlpatterns = [
    path('ruta1/', views.mi_vista_1, name='vista1'),
    # Otras rutas específicas de la app
]