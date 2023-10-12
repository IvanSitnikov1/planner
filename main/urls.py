from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('tasks-list/', TasksList.as_view(), name='tasks-list'),
    path('tasks-today/', TasksToday.as_view(), name='tasks-today'),
    path('archive/', Archive.as_view(), name='archive'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('create-subtask/<int:pk>/', CreateSubTask.as_view(), name='create-subtask'),
    path('detail-task/<int:pk>/', DetailTask.as_view(), name='detail-task'),
    path('detail-subtask/<int:pk>/', DetailSubTask.as_view(), name='detail-subtask'),
    path('comments/<int:pk>/', CreateAndReadComment.as_view(), name='comments'),
    path('update-task/<int:pk>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
    path('delete-subtask/<int:pk>/', delete_subtask, name='delete-subtask'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
