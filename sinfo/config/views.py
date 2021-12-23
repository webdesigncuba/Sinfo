'''
Vistas de Configuraciones
'''

# Django
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse

# Models
from .models import *

class MarcaListView(ListView):
    model = Marca

class MarcaCreateView(CreateView):
    model = Marca
    fields = ['nombre']

    def get_success_url(self):
        return reverse('marcalist')
