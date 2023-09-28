from django.shortcuts import render
# pages/views.py
from django.http import HttpResponse
from django.template import loader

def home_page_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello, World!")
