from django.db import models
from django.db.models.fields import BooleanField, CharField

# Create your models here.

class Task(models.Model):
    title = CharField(max_length=250)
    isCompleted = BooleanField(default=False,blank=True,null=True)

def __str__(self):
    return self.title