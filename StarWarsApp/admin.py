from django.contrib import admin

from StarWarsApp.models import Pelicula, Personaje, Raza

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Raza)
admin.site.register(Personaje)