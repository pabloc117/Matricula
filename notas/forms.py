from django import forms

from .models import *



class PensumForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pensum
        fields = ('alumno', 'gradonombre', 'gradoseccion', 'anio', 'materias')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.



def __init__ (self, *args, **kwargs):
    super(PensumForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

    self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget
    self.fields["materias"].help_text = "Ingrese las materias de este grado"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

    self.fields["materias"].queryset = Materia.objects.all()
