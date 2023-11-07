from django.contrib import admin
from django.urls import path
from appalumnos.views import saludo, miEdad, index, alumnos, busqueda_alumnos, busqueda_materias, materias, busqueda_docentes, docentes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('edad/<int:edad>/', miEdad),
     path('', index),
    path('frmalumnos', alumnos),
    path('frmbusqueda_alumnos', busqueda_alumnos),
    path('frmdocentes', docentes),
    path('frmbusqueda_docentes', busqueda_docentes),
    path('frmbusqueda_materias', busqueda_materias),
    path('frmmateria', materias)
]