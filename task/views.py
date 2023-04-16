from rest_framework import viewsets
from task.models import Task, AssignedTask
from task.serializers import TaskSerializer, AssignedTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AssignedTaskViewSet(viewsets.ModelViewSet):
    queryset = AssignedTask.objects.all()
    serializer_class = AssignedTaskSerializer
