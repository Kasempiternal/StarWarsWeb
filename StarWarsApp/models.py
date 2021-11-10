from django.db import models

# Create your models here.
class Pelicula(models.Model):
 nombre = models.CharField(max_length=40)
 año = models.IntegerField()
   
class Raza(models.Model):
 nombre = models.CharField(max_length=40)
 mundo = models.CharField(max_length=40)

class Personaje(models.Model):
 nombre = models.CharField(max_length=40)
 raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
 altura = models.FloatField()
 peliculas = models.ManyToManyField(Pelicula)




 