from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes, listar_cursos

# Son las URLS especificas de la app
urlpatterns = [
    path("estudiantes/", listar_estudiantes),
    path("cursos/", listar_cursos),
]
