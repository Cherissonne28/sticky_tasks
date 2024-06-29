
from django.db import models
from django.forms import fields, forms
from datetime  import  datetime, date



# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    saved = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    deadline = models.DateField(auto_now_add=False, auto_now=False, blank=True)
