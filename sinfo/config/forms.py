'''
Formularios del Modelo Config
'''

# Django
from django.forms import ModelForm

# Models
from .models import *

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
