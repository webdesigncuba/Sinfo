'''
Urls de Config
'''

# Django
from django.contrib import admin
from django.urls import path

# Views
from config.views import *
urlpatterns = [
    path('marca/list', MarcaListView.as_view(), name='marcalist'),
    path('marca/add', MarcaCreateView.as_view(), name='marcacreate'),
    path('marca/update/<pk>', MarcaUpdateView.as_view(), name='marcaupdate'),
    path('marca/delete/<pk>', MarcaDeleteView.as_view(), name='marcadelete'),
    path('departamento/list', DepartamentoListView.as_view(), name='arealist'),
    path('departamento/add', DepartamentoCreateView.as_view(), name='areacreate')
]