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
Vistas de Configuraciones
'''

# Django
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse
from django.urls import reverse_lazy

# Models
from .models import *

# Forms
from .forms import MarcaForm, DepartamentoForm

class MarcaListView(ListView):
    model = Marca
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de Marcas'
        return context

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'config/marca_form.html'
    success_url = reverse_lazy('marcalist')


    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)
        print(form.errors)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Creacion de Marcas'
        return context

    # def get_success_url(self):
    #     return reverse('marcalist')

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'config/marca_update.html'
    success_url = reverse_lazy('marcalist')


    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.object)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Marcas'
        return context


class MarcaDeleteView(DeleteView):
    model = Marca
    success_url = reverse_lazy('marcalist')


# Vistas Departamentos
class DepartamentoListView(ListView):
    model = Departamento
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de Areas'
        return context

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'config/despartamento_form.html'
    success_url = reverse_lazy('departamentolist')


    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)
        print(form.errors)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Creacion de Areas'
        return context


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'config/marca_update.html'
    success_url = reverse_lazy('arealist')


    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.object)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Areas'
        return context


class DepartamentoDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('arealist')