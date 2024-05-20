from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task


#from django.template import RequestContext
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect, csrf_exempt


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


""" def result(request, score):
    #tasks = Task.objects.all().values()
    template = loader.get_template('result.html')
    context = {
    #    'tasks':tasks,
        'score':score,
    }
    return HttpResponse(template.render(context,request)) """

#@csrf_protect
@csrf_exempt
def result(request):
    
    if request.method == 'POST':
        tasks = Task.objects.all().values()
        score = 0
        for task in tasks:
            ans = request.POST.get('id')
            if ans == task['answer']:
                score+=1
        template = loader.get_template('result.html')
        context = {
            'score':score,
        }
        return HttpResponse(template.render(context,request))
    

# Create your views here.
