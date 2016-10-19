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

    def get_queryset(self):
        """
        filter stuff for current user
        """
        user = self.request.user
        return TaskResult.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        """
        initialize task
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        data.user_id = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)