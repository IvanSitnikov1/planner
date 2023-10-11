from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from .models import *


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/index.html', context=context)


class TasksList(ListView):
    model = Task
    template_name = 'main/tasks_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачи'
        return context


class TasksToday(ListView):
    model = Task
    template_name = 'main/tasks_today.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(Q(deadline__lte=datetime.now()) & Q(active=True))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачи на сегодня'
        return context


class Archive(ListView):
    model = Task
    template_name = 'main/archive.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(active=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Архивные задачи'
        return context