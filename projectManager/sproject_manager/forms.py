from django.forms import ModelForm
from .models import Task, Project


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['start_date', 'end_date']


class ProjForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
