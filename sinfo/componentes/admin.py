'''
Admin de Componentes
'''

# Django
from django.contrib import admin

# Models
from .models import *

@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_filter = ('datos','marca')
    list_display = ('datos','marca')
    list_per_page = 10

@admin.register(PlacaBase)
class PlacaBaseAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns')
    list_filter = ('marca','modelo')
    list_per_page = 10

@admin.register(MemoriaRam)
class MemoriaRamAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns')
    list_filter = ('marca','modelo')
    list_per_page = 10

@admin.register(DiscoDuro)
class DiscoDuroAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns')
    list_filter = ('marca','modelo')
    list_per_page = 10

@admin.register(Fuente)
class FuenteAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns')
    list_filter = ('marca','modelo')
    list_per_page = 10


