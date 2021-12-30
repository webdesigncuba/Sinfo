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
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import context
from django_renderpdf.views import PDFView
from django.contrib import messages


# Models
from .models import *

# Forms
from .forms import *

class ChasisListView(ListView):
    model = Chasis
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de Chasis'
        return context

class ChasisCreateView(CreateView):
    model = Chasis
    form_class = ChasisForm
    template_name = 'perifericos/chasis_form.html'
    success_url = reverse_lazy('chasislist')


    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = ChasisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guardado exitoso')
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)
        print(form.errors)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Creacion de Chasis'
        return context

    # def get_success_url(self):
    #     return reverse('marcalist')

class ChasisUpdateView(UpdateView):
    model = Chasis
    form_class = ChasisForm
    template_name = 'perifericos/chasis_update.html'
    success_url = reverse_lazy('chasislist')


    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.object)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Chasis'
        return context


class ChasisDeleteView(DeleteView):
    model = Chasis
    success_url = reverse_lazy('chasislist')

class ChasisPDF(PDFView):
    template_name = 'report.html'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)

        context['chasis'] = Chasis.objects.all()

        return context



