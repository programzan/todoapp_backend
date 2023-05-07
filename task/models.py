from django.contrib.auth import get_user_model
from django.db import models
from core.models import DefaultDateFieldsAbstractClass

User = get_user_model()


class Task(DefaultDateFieldsAbstractClass):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class AssignedTask(DefaultDateFieldsAbstractClass):
    task = models.ForeignKey(
        Task,
        verbose_name='Задача',
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
    )
    assignee = models.ForeignKey(
        User,
        verbose_name='Исполнитель',
        on_delete=models.CASCADE,
        related_name='related_user_tasks',
    )
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Выданная задача'
        verbose_name_plural = 'Выданные задачи'
