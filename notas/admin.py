from django.contrib import admin
from notas.models import *

#Registramos nuestras clases principales.
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Pensum, PensumAdmin)

# Register your models here.
