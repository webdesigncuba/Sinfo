'''
Vista Principal del Sistem
'''
# Django
from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {'version': settings.VERSION}
    return render(request,'index.html', context)


