from django.shortcuts import render
from django.http import HttpResponse


def inicio (request):
    return render(request, "curso.html ")

def estudiantes(request):
    return HttpResponse("estudiante")

def profesores(request):
    return HttpResponse("profesores")

def entregables(request):
    return HttpResponse("entregables")