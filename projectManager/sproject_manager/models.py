from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    expected_end_date = models.DateTimeField(blank=True, null=True)
    status_choices = (
        ("ACTIVE", "ACTIVE"),
        ("PENDING", "PENDING"),
        ("CLOSED", "CLOSED"),
    )
    status = models.CharField(
        max_length=7,
        choices=status_choices,
        default="PENDING",
    )
    author = models.CharField(max_length=30)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    complete_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=30)


    def __str__(self):
        return self.name