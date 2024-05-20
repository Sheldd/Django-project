from django.db import models

# Create your models here.

class Task(models.Model):
    section = models.CharField(max_length = 50)
    task = models.TextField()
    answer = models.IntegerField()