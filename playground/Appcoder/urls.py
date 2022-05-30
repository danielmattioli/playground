from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("curso/", views.curso),
   # path("profesores", views.profesores),
   # path("estudiante", views.estudiantes),
   # path("entregables", views.entregables)
]