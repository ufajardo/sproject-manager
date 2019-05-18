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

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    status_choices = (
        ("ACTIVE", "ACTIVE"),
        ("PENDING", "PENDING"),
        ("CLOSED", "CLOSED"),
    )
    status = models.CharField(
        max_length=7,
        choices=status_choices,
        default="ACTIVE",
    )
    author = models.CharField(max_length=30)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def status_closed(self):
        self.status.choices = "CLOSED"
