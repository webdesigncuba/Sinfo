'''
Urls de Config
'''

# Django
from django.contrib import admin
from django.urls import path

# Views
from config.views import *
urlpatterns = [
    path('list', MarcaListView.as_view(), name='marcalist'),
    path('list/add', MarcaCreateView.as_view(), name='marcacreate'),
]