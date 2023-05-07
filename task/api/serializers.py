from rest_framework import serializers

from core.api.serializers import UserNameSerializer
from task.models import Task, AssignedTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AssignedTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    assignee = UserNameSerializer()

    class Meta:
        model = AssignedTask
        fields = '__all__'
