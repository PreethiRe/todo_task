from django.db import models
from django.contrib import admin
import csv
from django.http import HttpResponse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 45)
    description = models.CharField(max_length = 100)
    status = models.CharField(max_length = 15)
    task_datetime = models.DateTimeField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "todo_task"
