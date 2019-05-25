from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import generics, viewsets
import django_filters.rest_framework
from .serializers import ProjectSerializer, TaskSerializer
from .models import Project, Task
from .forms import TaskForm, ProjForm
# Create your views here.

def index(request):
    project_list = Project.objects.all()
    task_list = Task.objects.all()

    context = {
        'project_list': project_list,
        'task_list': task_list,
    }

    return render(request, 'sproject_manager/index.html', context)


def create_task(request):
    task = TaskForm(request.POST or None)

    if task.is_valid():
        task.save()
        return redirect('project_manager:index')

    context = {
        'taskform': task
    }

    return render(request, 'sproject_manager/task-create.html', context)


def create_proj(request):
    proj = ProjForm(request.POST or None)

    if proj.is_valid():
        proj.save()
        return redirect('project_manager:index')

    context = {
        'proj': proj
    }

    return render(request, 'sproject_manager/proj-create.html', context)


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    taskform = TaskForm(request.POST or None, instance=task)

    if request.POST:
        if taskform.is_valid():
            data = request.POST.copy()
            status = data.get('status')
            if status == "ACTIVE":
                obj = taskform.save(commit=False)
                obj.start_date = timezone.now()
                obj.save()
                return redirect('project_manager:index')
            elif status == "CLOSED":
                obj = taskform.save(commit=False)
                obj.end_date = timezone.now()
                obj.save()
                return redirect('project_manager:index')
            elif status == "PENDING":
                taskform.save()
                return redirect('project_manager:index')

    context = {
        'task': task,
        'taskform': taskform
    }

    return render(request, 'sproject_manager/task-details.html', context)



def proj_details(request, id):
    proj = get_object_or_404(Project, id=id)
    task_list = Task.objects.filter(project=id)

    context = {
        'proj': proj,
        'task_list': task_list,
    }

    return render(request, 'sproject_manager/proj-details.html', context)



class ProjectList(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id']
        return Task.objects.filter(project=id)

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.POST:
        Task.objects.filter(id=id).delete()
        return redirect('project_manager:index')

    context = {
        'task': task,
    }

    return render(request, 'sproject_manager/task-delete.html', context)