from rest_framework import serializers
from task.models import Task, AssignedTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AssignedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedTask
        fields = '__all__'
