from django.conf.urls import url, include
from . import views



#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^pensum/nuevo/$', views.pensum_nuevo, name='pensum_nuevo'),
    ]
