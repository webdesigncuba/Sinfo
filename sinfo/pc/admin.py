'''
Admin de Pc
'''

# Django
from django.contrib import admin

# Models
from .models import *

@admin.register(Pc)
class PcAdmin(admin.ModelAdmin):
    list_display = ('fecha','area','so','sello','num')
    list_filter = ('fecha','area')
    list_per_page =10
