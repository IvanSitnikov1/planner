from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('tasks-list', TasksList.as_view(), name='tasks-list'),
    path('tasks-today', TasksToday.as_view(), name='tasks-today'),
    path('archive', Archive.as_view(), name='archive'),
]
