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
Modelo de datos de las PC del sistema
'''

# Django
from django.db import models

# Modelos
from componentes.models import *
from perifericos.models import *
from software.models import *
from config.models import Departamento

class Pc(models.Model):
    fecha = models.DateField('Fecha de Creacion del Expediente', auto_now_add=True)
    area = models.ForeignKey(Departamento, verbose_name='Area de la PC', on_delete=models.CASCADE)
    num = models.IntegerField('Numeo de Expediente', default=1)
    inv_torre = models.CharField('Inventario de la Torre', max_length=100)
    chasis = models.ForeignKey(Chasis, verbose_name='Chasis de la PC', on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, verbose_name='CPU de la PC', on_delete=models.CASCADE)
    mb = models.ForeignKey(PlacaBase, verbose_name='Mother Board de la PC', on_delete=models.CASCADE)
    memoria = models.ForeignKey(MemoriaRam, verbose_name='Memoria Ram de la PC', on_delete=models.CASCADE)
    teclado = models.ForeignKey(Teclado, verbose_name='Teclado de la PC', on_delete=models.CASCADE)
    mause = models.ForeignKey(Mause, verbose_name='Mause de la PC', on_delete=models.CASCADE)
    bocinas = models.ForeignKey(Bocinas, verbose_name='Bocinas Duro de la PC', on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, verbose_name='Monitor de la PC', on_delete=models.CASCADE)
    ups = models.ForeignKey(UPS, verbose_name='UPS de la PC', on_delete=models.CASCADE)
    impresora = models.ForeignKey(Impresora, verbose_name='Impresora de la PC', on_delete=models.CASCADE)
    so = models.ForeignKey(SO, verbose_name='Sistema Operativo  de la PC', on_delete=models.CASCADE)
    sello = models.CharField('Sello de PC', max_length=100, unique=True)
    otros = models.CharField('Otros Datos de Interes', max_length=255, default='')

    def __str__(self):
        return self.inv_torre


