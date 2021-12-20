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

    def __str__(self):
        return self.inv_torre


