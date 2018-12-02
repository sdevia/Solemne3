# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
from .models import Adoptante
from django.http import HttpResponse

# Create your views here.

def inscripcion(request):
    correo = request.POST.get('correo', 0)
    run = request.POST.get('rut',0)
    nombres = request.POST.get('nombres','')
    apellido = request.POST.get('apellidos','')
    nacimiento = request.POST.get('nacimiento',0)
    icon_telephone = request.POST.get('icon_telephone',0)
    regiones = request.POST.get('regiones',0)
    comunas = request.POST.get('comunas',0)
    tipo = request.POST.get('tipoVivienda',0)
    adoptante = Adoptante(Email = correo, Rut = run, Nombre = nombres, Apellidos = apellido, FechaNacimiento = nacimiento, Telefono = icon_telephone, Region = regiones, Ciudad = comunas, TipoVivienda = tipo)
    adoptante.save()
    return render(request,'inscripcion.html')


def index(request):
    response = requests.get('http://api.ipstack.com/check?access_key=ed45289eb6aa84378442d6c312320945')
    data = response.json()
    
    return render(request,'index.html',{'latitud': data['latitude'],'longitud': data['longitude'],'ciudad': data['city'],'region': data['region_code'],'ip': data['ip'], 'pais': data['country_name'] })    
