from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola desde django")

def miEdad(request, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)

def index(request):
    return render(request, 'index.html')

def alumnos(request):
    return render(request, 'alumnos.html')

def busqueda_alumnos(request):
    return render(request, 'busqueda_alumnos.html')

def docentes(request):
    return render(request, 'docentes.html')

def busqueda_docentes(request):
    return render(request, 'busqueda_docentes.html')

def materias(request):
    return render(request, 'materias.html')

def busqueda_materias(request):
    return render(request, 'busqueda_materias.html')