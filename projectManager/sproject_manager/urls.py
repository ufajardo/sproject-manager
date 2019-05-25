"""projectManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from . import views
from django.urls import path, include

project_list = views.ProjectList.as_view({
    'get': 'list',
})

app_name = 'project_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-task/', views.create_task, name='create-task'),
    path('create-proj/', views.create_proj, name='create-proj'),
    path('api/project/', project_list, name='api-proj'),
    path('api/project/<int:id>/', project_list, name='api-proj'),
    path('task-details/<int:id>/', views.update_task, name='update-task'),
    path('proj-details/<int:id>/', views.proj_details, name='proj-details'),
    path('task-delete-confirm/<int:id>/', views.delete_task, name='delete-task'),
]
