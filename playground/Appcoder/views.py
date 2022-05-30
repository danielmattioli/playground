from django.shortcuts import render
from django.http import HttpResponse


def curso (request):
    text= f"Esto funciona"
    return HttpResponse(text)

def estudiantes(request):
    return HttpResponse("estudiante")

def profesores(request):
    return HttpResponse("estudiante")

def entregables(request):
    return HttpResponse("estudiante")