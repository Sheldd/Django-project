#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def quiz(request):
    return HttpResponse("Hello world!")
    

# Create your views here.
