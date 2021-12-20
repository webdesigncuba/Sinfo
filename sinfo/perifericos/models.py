'''
Modelos de datos de los Perifericos del Sistema
'''

# Django
from django.db import models
from config.models import Marca

class Chasis(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca del Chasis', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Chasis',max_length=100)
    ns = models.CharField('Numero de serie del Chasis', max_length=100)

    def __str__(self):
        return self.marca

class Teclado(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Teclado', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Teclado', max_length=100)
    ns = models.CharField('Serial de Teclado', max_length=100)
    inventario = models.CharField('Invenatrio de Teclado', max_length=100)

    def __str__(self):
        return self.inventario

class Mause(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Mause', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Mause', max_length=100)
    ns = models.CharField('Serial de Mause', max_length=100)
    inventario = models.CharField('Inventario de Mause', max_length=100)

    def __str__(self):
        return self.inventario

class UPS(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la UPS', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del UPS', max_length=100)
    ns = models.CharField('Serial de UPS', max_length=100)
    inventario = models.CharField('Inventario de UPS', max_length=100)

    def __str__(self):
        return self.inventario

class Impresora(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Impresora', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Impresora', max_length=100)
    ns = models.CharField('Serial de Impresora', max_length=100)
    inventario = models.CharField('Inventario de Impresora', max_length=100)

    def __str__(self):
        return self.inventario

class Monitor(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Monitor', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Monitor', max_length=100)
    ns = models.CharField('Serial de Monitor', max_length=100)
    inventario = models.CharField('Inventario de Monitor', max_length=100)

    def __str__(self):
        return self.inventario

class Bocinas(models.Model):
    marca = models.ForeignKey(Marca, verbose_name='Marca de la Bocinas', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo del Bocinas', max_length=100)
    ns = models.CharField('Serial de Bocinas', max_length=100)
    inventario = models.CharField('Inventario de Bocinas', max_length=100)

    def __str__(self):
        return self.inventario