'''
<<<<<<< HEAD
Formularios del Modelo Config
'''

# Django
from django import forms

# Models
from .models import *

class MarcaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for forms in self.visible_fields():
            forms.field.widget.attrs['class']='form-control'
    class Meta:
        model = Marca
        fields = '__all__'
        labels = {
            'name': 'Nombre'
        }


