from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http


def saludar_con_html(request):
    contexto = {
        "profesor": "Pedro",
        "tutores": ["Mariano", "Ariel"],
        "comision": 55350,
    }
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response


def listar_estudiantes(request):
    contexto = {
        "profesor": "Pedro",
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel", "nota": 10},
            {"nombre": "Manuela", "apellido": "Gomez", "nota": 4},
            {"nombre": "Ivan", "apellido": "Tomasevich", "nota": 6},
            {"nombre": "Carlos", "apellido": "Perez", "nota": 1},
        ]
    }
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response
