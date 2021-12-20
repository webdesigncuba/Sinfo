'''
Modelos datos COmponentes del Sistema
'''

# Django
from django.db import models

# Models
from config.models import Marca

class CPU(models.Model):
    datos = models.CharField('Datos Generales del Micro procesador', max_length=100)
    marca = models.ForeignKey(Marca, verbose_name='Marca del Procesador', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'CPU'

    def __str__(self):
        return '%s - %s' % (self.marca, self.datos)

class PlacaBase(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Mother Board', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del MotherBoard', max_length=100)
    ns = models.CharField('Serial del MotherBoard', max_length=100)

    class Meta:
        verbose_name_plural = 'Mother Boards'

    def __str__(self):
        return '%s - %s' % (self.marca, self.modelo)

class MemoriaRam(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Memoria', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Memoria', max_length=100)
    ns = models.CharField('Serial de Memoria', max_length=100)
    capacidad = models.IntegerField('Capacidad de la Memoria Ram')

    class Meta:
        verbose_name_plural = 'Memorias Ram'

    def __str__(self):
        return '%s - %s' % (self.marca, self.ns)

class DiscoDuro(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Disco', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Disco', max_length=100)
    ns = models.CharField('Serial de Disco', max_length=100)
    capacidad = models.IntegerField('Capacidad de la Disco')

    class Meta:
        verbose_name_plural = 'Discos Duros'

    def __str__(self):
        return '%s - %s' % (self.marca, self.ns)

class Fuente(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Fuente', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Fuente', max_length=100)
    ns = models.CharField('Serial de Fuente', max_length=100)

    def __str__(self):
        return '%s - %s' % (self.marca, self.ns)

