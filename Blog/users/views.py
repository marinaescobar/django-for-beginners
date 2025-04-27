from django.shortcuts import render

from django.http import HttpResponse #Devuelve una respuesta

def login(request):
    
    return HttpResponse("Hola, estás en el login")

def register(request):
    
    return HttpResponse("Hola, estás en el registro")
