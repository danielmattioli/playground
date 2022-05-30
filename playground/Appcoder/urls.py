from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("curso", views.inicio),
    path("profesores", views.profesores),
    path("estudiantes", views.estudiantes),
    path("entregables", views.entregables)
]