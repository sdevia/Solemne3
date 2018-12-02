# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Adoptante (models.Model):
    Email = models.CharField(max_length=30)
    Rut = models.CharField(max_length=30)
    Nombre = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=40)
    FechaNacimiento = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=30)
    Region = models.CharField(max_length=30, default='Región Metropolitana de Santiago')
    Ciudad = models.CharField(max_length=30)
    TipoVivienda = models.CharField(max_length=50)
