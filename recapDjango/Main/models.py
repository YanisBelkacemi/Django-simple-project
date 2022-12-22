from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class item(models.Model):
    key = models.ForeignKey(todolist,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    done = models.BooleanField()
    def __str__(self):
        return self.text