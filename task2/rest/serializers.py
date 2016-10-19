from task2.rest.models import TaskResult
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('task_name', 'args', 'task_result')
