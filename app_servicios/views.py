from django.shortcuts import render
from app_servicios.models import servicio

def servicios(request):

    servicios = servicio.objects.all()

    return render(request, 'Bservicios.html', { "servicios" : servicios})

