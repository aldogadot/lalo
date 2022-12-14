from django.http import HttpResponse
import datetime
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def cursoCss(request):
    fecha = datetime.datetime.now()
    return render(request,"cursoCss.html",{"fecha":fecha})
def cursoC(request):
    fecha = datetime.datetime.now()
    return render(request,"CursoC.html",{"fecha":fecha})
def saludo(request):
    p1 = Persona(" Profesor Juan","Barrón")
    temas = ["Plantillas", "Modelos","Vitas","despliegue"]
    fecha = datetime.datetime.now()

    return render(request,"saludo.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha":fecha, "temas":temas})

def despedida(request):
   return HttpResponse("Adios amigos del youtube")

def fecha(request):
    fecha_actual = datetime.datetime.now()

    hora = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(hora)

def calculaEdad(request,edad,year):
    periodo = year - 2022
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(year,edadFutura)

    return HttpResponse(documento)

def laloLegal (request, edad):
    if (edad>=18):
        return HttpResponse("Lalo legal")
    else:
        return HttpResponse("Lalo ilegal")