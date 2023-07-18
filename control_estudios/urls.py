from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes

# Son las URLS especificas de la app
urlpatterns = [
    path("estudiantes/", listar_estudiantes),
]
