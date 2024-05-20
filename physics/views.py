#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def quiz(request):
    tasks = Task.objects.all().values()
    template = loader.get_template('quiz.html')
    context = {
        'tasks':tasks,
    }
    return HttpResponse(template.render(context,request))


def result(request):
    tasks = Task.objects.all().values()
    template = loader.get_template('result.html')
    context = {
        'tasks':tasks,
    }
    return HttpResponse(template.render(context,request))
  

# Create your views here.
