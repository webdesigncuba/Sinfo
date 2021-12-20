'''
Admin de Software
'''

# Django
from django.contrib import admin

# Models
from .models import *

@admin.register(SO)
class SOAdmin(admin.ModelAdmin):
    list_display = ('marca','version','tipo')
    list_filter = ('marca','tipo',)
    list_per_page = 10
