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

# Django
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy

# Vista Software

# Models
from .models import SO

#Forms
from .forms import SOForm

class SOListView(ListView):
    model = SO
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de Software'
        return context

class SOCreateView(CreateView):
    model = SO
    form_class = SOForm
    template_name = 'software/'
    success_url = reverse_lazy('marcalist')


    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = SOForm(request.POST)
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
        context['title']='Creacion de Software'
        return context

class SOUpdateView(UpdateView):
    model = SO
    form_class = SOForm
    template_name = 'config/so_update.html'
    success_url = reverse_lazy('softwarelist')


    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.object)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Software'
        return context


class SODeleteView(DeleteView):
    model = SO
    success_url = reverse_lazy('softwarelist')