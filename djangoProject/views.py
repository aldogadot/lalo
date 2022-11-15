from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
    doc_externo = open(r"C:\Users\aldo_\Documents\lalo\djangoProject\plantillas\saludo.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

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