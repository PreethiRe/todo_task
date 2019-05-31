"""crud URL Configuration

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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),#admin interface
    path('home/', views.home,name="home"),#home page which displays todo task and can add,edit,delete todo task
    path('todo/', views.todo,name="todo"),#html form for adding todo task
    path('task/', views.task,name="task"),#add todo task
    path('task_delete/<int:task_id>/', views.task_delete,name="task_delete"),#delete task based on id
    path('task_edit/<int:task_id>/', views.task_edit,name="task_edit"),
    path('task_update/', views.task_update,name="task_update"),#updating particular task
]
