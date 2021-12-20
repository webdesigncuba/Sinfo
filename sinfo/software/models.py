'''
Modelo de datos de Software del Sistema
'''

#Django
from django.db import models

# Modelos
from config.models import Marca

class SO(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca del Software', on_delete=models.CASCADE)
    version = models.CharField('Version del Software', max_length=100)
    tipo = models.CharField('Tipo de Software', max_length=100, default='')

    class Meta:
        verbose_name_plural='Softwares'

    def __str__(self):
        return str(self.marca)
