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
Admin de los Perifericos
'''

# Django
from django.contrib import admin

# Models
from .models import *

@admin.register(Chasis)
class ChasisAdmin(admin.ModelAdmin):
    icon_name = 'devices' 
    list_display = ('marca','modelo','ns')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Teclado)
class TecladoAdmin(admin.ModelAdmin):
    icon_name = 'keyboard' 
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Mause)
class MauseAdmin(admin.ModelAdmin):
    icon_name = 'mouse' 
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Bocinas)
class BocinasAdmin(admin.ModelAdmin):
    icon_name = 'speaker' 
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    icon_name = 'desktop_windows' 
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

@admin.register(Impresora)
class ImpresoraAdmin(admin.ModelAdmin):
    icon_name = 'local_printshop' 
    list_display = ('marca','modelo','ns','inventario')
    list_filter = ('marca',)
    list_per_page = 10

