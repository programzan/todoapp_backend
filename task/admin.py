from django.contrib import admin
from task.models import Task, AssignedTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(AssignedTask)
class AssignedTaskAdmin(admin.ModelAdmin):
    pass
