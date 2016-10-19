from rest_framework import status
from rest_framework.response import Response
from task2.rest.models import TaskResult
from rest_framework import viewsets
from task2.rest.serializers import *
from task2.rest.utils.math_utils import *
from task2.rest.utils.ping_utils import *


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
        """
        data = request.data
        data["user_id"] = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # task execution
        task_result = 0
        post_args = request.data["args"]
        if request.data["task_name"] == "nth_prime":
            task_result = find_nth_prime(int(post_args))
        elif request.data["task_name"] == "factorize":
            task_result = factorize(int(post_args))
        elif request.data["task_name"] == "ping":
            argv = post_args.split(" ")
            hostname = argv[0]
            times = int(argv[1])
            task_result = ping(hostname, times)

        serializer.save(user=request.user, task_result=task_result)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)