'''
Modelos de datos de la configtuacion del Sistema
'''

# Django
from django.db import models

class Departamento(models.Model):
    nombre = models.CharField('Nombre del Departamento', max_length=100)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
