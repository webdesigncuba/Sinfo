'''
Admin de la Cofiguracion del Sistema
'''

# Django
from django.contrib import admin

# Models
from .models import *

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    list_per_page = 10

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    list_per_page = 10

