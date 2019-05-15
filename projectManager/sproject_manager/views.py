from django.shortcuts import render, get_object_or_404
from .models import Project, Task

# Create your views here.

def index(request):
    project_list = Project.objects.all()
    task_list = Task.objects.all()


    context = {
        'project_list': project_list,
        'task_list': task_list,
    }
    return render(request, 'sproject_manager/index.html', context)


def task_item(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        if 'delete' in request.POST:
            task.delete()
            return render(request, 'sproject_manager/index.html')

    context = {
        'task': task,
    }

    return render(request, 'sproject_manager/task-details.html', context)