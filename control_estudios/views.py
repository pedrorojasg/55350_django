from django.shortcuts import render

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
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "cursos": [
            {"nombre": "Fisica", "comision": 1000},
            {"nombre": "Python", "comision": 55350},
            {"nombre": "Redes Sociales", "comision": 2000},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response
