# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Vacuna(models.Model):
    Nombre = models.CharField(max_length=40)


class Rescatado(models.Model):
    Codigo = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=20)
    Tamano = models.CharField(max_length=4)
    Peso = models.CharField(max_length=4)
    Color = models.CharField(max_length=7)
    Descripcion = models.TextField()
    FechaRescate = models.DateField()
    Estado = models.CharField(max_length=32)
    vacuna = models.ManyToManyField(Vacuna)







