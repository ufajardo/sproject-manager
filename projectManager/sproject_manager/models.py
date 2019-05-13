from django.db import models
import datetime
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    complete_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=30)
#    collaborators = models.ManyToManyField()


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    complete_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=30)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


