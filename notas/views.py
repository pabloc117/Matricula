from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from .forms import PensumForm
from notas.models import Pensum, Materia,Asignacion
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#Vista para insertar una nueva película y los actores que actúan en ella.



#Sólo código:

def pensum_nuevo(request):
    if request.method == "POST":
        formulario = PensumForm(request.POST)
        if formulario.is_valid():
            pensum = Pensum.objects.create(alumno=formulario.cleaned_data['alumno'],gradonombre=formulario.cleaned_data['gradonombre'],gradoseccion=formulario.cleaned_data['gradoseccion'], anio = formulario.cleaned_data['anio'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, pensum_id = pensum.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pensum Guardado Exitosamente')
    else:
        formulario = PensumForm()
    return render(request, 'pelicula/pelicula_editar.html', {'formulario': formulario})
