'''
Admin de los Perifericos
'''

# Django
from django.contrib import admin

# Models
from .models import *

@admin.register(Chasis)
class ChasisAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Teclado)
class ChasisAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Mause)
class ChasisAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Bocinas)
class ChasisAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Monitor)
class ChasisAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Impresora)
class ChasisAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

