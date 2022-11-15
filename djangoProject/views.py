from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola perrillos")

def despedida(request):
    return  HttpResponse("Adios lalito perro")