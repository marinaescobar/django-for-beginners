from django.shortcuts import render
from django.http import HttpResponse #Devuelve una respuesta

def manage_post(request):
    return HttpResponse("¡Bienvenido a la página de Manage Post!")
