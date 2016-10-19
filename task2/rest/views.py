from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task2.rest.models import TaskResult

from rest_framework import viewsets
from task2.rest.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskResult.objects.all()
    serializer_class = TaskSerializer

