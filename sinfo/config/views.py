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