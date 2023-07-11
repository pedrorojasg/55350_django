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
