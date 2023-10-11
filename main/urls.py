from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('tasks-list/', TasksList.as_view(), name='tasks-list'),
    path('tasks-today/', TasksToday.as_view(), name='tasks-today'),
    path('archive/', Archive.as_view(), name='archive'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('detail-task/<int:pk>/', DetailTask.as_view(), name='detail-task'),
    path('update-task/<int:pk>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
