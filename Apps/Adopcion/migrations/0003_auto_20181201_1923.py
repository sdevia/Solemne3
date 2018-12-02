# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adopcion', '0002_auto_20181110_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Rut', models.IntegerField()),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=40)),
                ('FechaNacimiento', models.DateField()),
                ('Edad', models.IntegerField()),
                ('Telefono', models.CharField(max_length=10)),
                ('Ciudad', models.CharField(max_length=30)),
                ('Domicilio', models.CharField(max_length=50)),
                ('TipoVivienda', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]