from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.db.models import Q

from .models import *
from .forms import *


class CreateTask(CreateView):
    form_class = CreateTaskForm
    template_name = 'main/create_task.html'
    success_url = reverse_lazy('tasks-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание задачи'
        return context


class DetailTask(DetailView):
    model = Task
    template_name = 'main/detail_task.html'
    context_object_name = 'task'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание задачи'
        return context


class UpdateTask(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'main/update_task.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование задачи'
        return context


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('tasks-list')


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'main/index.html', context=context)


class TasksList(ListView):
    model = Task
    template_name = 'main/tasks_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(active=True).order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачи'
        return context


class TasksToday(ListView):
    model = Task
    template_name = 'main/tasks_today.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(
        Q(deadline__lte=datetime.now()) & Q(active=True)
    ).order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачи на сегодня'
        return context


class Archive(ListView):
    model = Task
    template_name = 'main/archive.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(active=False).order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Архивные задачи'
        return context