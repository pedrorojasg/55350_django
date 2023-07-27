from django.contrib import admin
from django.urls import path

from control_estudios.views import (
    listar_cursos, crear_curso, buscar_cursos, eliminar_curso,
    editar_curso, EstudianteListView, EstudianteCreateView,
    EstudianteDetailView, EstudianteUpdateView, EstudianteDeleteView
)

# Son las URLS especificas de la app
urlpatterns = [
    # URLS de cursos
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de estudiantes
    path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
]
