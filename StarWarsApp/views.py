from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse

from StarWarsApp.models import Personaje
# Create your views here.

def home(request):
  # personajes = get_list_or_404(Personaje.objects.order_by('altura'))
# personajeMain = get_object_or_404(Personaje, personaje_id)

   return render(request,'home.html')