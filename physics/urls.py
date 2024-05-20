from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/result/',views.result, name='result'),
]