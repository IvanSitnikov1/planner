from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Высокий - 1'),
        (2, 'Средний - 2'),
        (3, 'Низкий - 3'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    active = models.BooleanField(default=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=255)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    subtask = models.ForeignKey('SubTask', on_delete=models.CASCADE, blank=True, null=True)


class SubTask(models.Model):
    content = models.TextField()
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)