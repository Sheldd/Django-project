from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task




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

@csrf_exempt
def result(request):
    
    if request.method == 'POST':
        tasks = Task.objects.all().values()
        score = 0
        for task in tasks:
            rs = task['id']
            ans = request.POST.get(f'{rs}')
            #print(ans, task['answer'])
            
            if str(ans) == str(task['answer']):
                score+=1
        template = loader.get_template('result.html')
        
        context = {
            'score':score,
        }
        return HttpResponse(template.render(context,request))
    

# Create your views here.
