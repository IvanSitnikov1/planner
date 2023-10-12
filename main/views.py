from datetime import datetime

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.db.models import Q

from .models import *
from .forms import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


def logout_user(request):
    logout(request)
    return redirect('login')


class CreateTask(CreateView):
    form_class = CreateTaskForm
    template_name = 'main/create_task.html'
    success_url = reverse_lazy('tasks-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание задачи'
        return context

    def form_valid(self, form):
        task = form.save(commit=False)
        author = self.request.user.username
        task.author = author
        task.save()
        return redirect(reverse('detail-task', kwargs={'pk': task.pk}))


class CreateSubTask(CreateView):
    form_class = CreateSubTaskForm
    template_name = 'main/create_subtask.html'
    success_url = reverse_lazy('tasks-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание подзадачи'
        pk = self.kwargs['pk']
        context['pk'] = pk
        return context

    def form_valid(self, form):
        subtask = form.save(commit=False)
        pk = self.kwargs['pk']
        task = Task.objects.get(pk=pk)
        subtask.task = task
        subtask.save()
        return redirect(reverse('detail-task', kwargs={'pk': pk}))


class DetailTask(DetailView):
    model = Task
    template_name = 'main/detail_task.html'
    context_object_name = 'task'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Описание задачи'
        pk = self.kwargs['pk']
        subtasks = SubTask.objects.filter(task__pk=pk)
        context['subtasks'] = subtasks
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


def delete_subtask(request, pk):
    subtask = SubTask.objects.get(pk=pk)
    subtask.delete()
    return redirect(request.META.get('HTTP_REFERER'))


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
    template_name = 'main/tasks_list.html'
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
    template_name = 'main/tasks_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(active=False).order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Архивные задачи'
        return context