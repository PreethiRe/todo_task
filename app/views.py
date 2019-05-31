from django.shortcuts import render
from django.http import HttpResponse
from app.models import Task
from django.contrib import admin
from django.utils.dateparse import  parse_datetime


# Create your views here.
#home page which displays all todo tasks
def home(request):
    todo_task = Task.objects.exclude(status=u'D')

    return render(request, "home.html", {"res": todo_task})


def todo(request):
    return render(request, "todo.html")

#delete tasks
def task_delete(request, task_id):
    Task.objects.filter(id=task_id).update(status="D")
    todo_task = Task.objects.exclude(status=u'D')

    return render(request, "home.html", {"res": todo_task})


def task_edit(request, task_id):
    task_data = Task.objects.filter(id=task_id)
    return render(request, "todo.html", {"res": task_data})

#updating particular task
def task_update(request):
    title = request.POST['title']
    task_id = request.POST['task_id']
    description = request.POST.get('desc')
    status = request.POST['status']
    task_datetime = request.POST['datetime_']
    task_datetime = parse_datetime(task_datetime)
    Task.objects.filter(id=task_id).update(title=title, description=description, status=status,
                                           task_datetime=task_datetime)

    todo_task = Task.objects.exclude(status=u'D')

    return render(request, "home.html", {"res": todo_task})


# adding todo tasks
def task(request):
    if request.method == "POST":
        task_data = Task()
        task_data.title = request.POST['title']
        task_data.description = request.POST.get('desc')
        task_data.status = request.POST['status']
        task_datetime = request.POST['datetime_']
        task_data.task_datetime = parse_datetime(task_datetime)
        task_data.save()
        todo_task = Task.objects.exclude(status=u'D')

        return render(request, "home.html", {"res": todo_task})
