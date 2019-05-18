from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import TaskForm
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
        'task': task
    }

    return render(request, 'sproject_manager/task-create.html', context)


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    taskform = TaskForm(request.POST or None, instance=task)

    if request.POST:
        if taskform.is_valid():
            taskform.save()
            return redirect('project_manager:index')

    context = {
        'task': task,
        'taskform': taskform
    }

    return render(request, 'sproject_manager/task-details.html', context)


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.POST:
        Task.objects.filter(id=id).delete()
        return redirect('project_manager:index')

    context = {
        'task': task,
    }

    return render(request, 'sproject_manager/task-delete.html', context)