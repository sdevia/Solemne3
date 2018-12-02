# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Rescatado, Vacuna

# Register your models here.

admin.site.register(Rescatado)
admin.site.register(Vacuna)
