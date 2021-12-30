#
# Created on Sat Dec 25 2021
#
# The MIT License (MIT)
# Copyright (c) 2021 David Cordero Rosales
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

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
    inv = models.CharField('Numero de Inventario', max_length=100, default='', unique=True)

    def __str__(self):
        return str(self.marca)

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