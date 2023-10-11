from django.db import models
from django.urls import reverse_lazy


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Высокий - 1'),
        (2, 'Средний - 2'),
        (3, 'Низкий - 3'),
    ]
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    deadline = models.DateField(verbose_name='Срок выполнения')
    active = models.BooleanField(default=True, verbose_name='Активно')
    comments = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Комментарии'
    )
    author = models.CharField(max_length=255, verbose_name='Автор')
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        verbose_name='Приоритет'
    )
    subtask = models.ForeignKey(
        'SubTask',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Заголовок'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('detail-task', kwargs={'pk': self.pk})


class SubTask(models.Model):
    content = models.TextField(verbose_name='Контент')
    active = models.BooleanField(default=True, verbose_name='Активно')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')


class Comment(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)