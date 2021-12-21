'''
Vistas de Configuraciones
'''

# Django
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse

# Models
from .models import *

# Form
from .forms import MarcaForm

class MarcaListView(ListView):
    model = Marca

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'config/marca_form.html'

    def get_success_url(self):
        return reverse('marcalist')
