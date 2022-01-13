from django.shortcuts import render

from django.http import HttpResponse
from .models import Curso
def crearCurso (request, camadaa):
    curso = Curso(nombre='Diseño web', camada=camadaa)
    curso.save()
    txt= f"Curso----> {curso.nombre} camada---> {curso.camada}"
    return HttpResponse (txt)

