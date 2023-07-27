from django.contrib import admin
from django.urls import path

from control_estudios.views import (
    listar_estudiantes, listar_cursos, crear_curso, buscar_cursos, eliminar_curso,
    editar_curso
)

# Son las URLS especificas de la app
urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
]
