from django.contrib.auth.models import User
from django.db import models


class TaskResult(models.Model):
    task_name = models.CharField(max_length=20)
    task_result = models.TextField(max_length=20)
    user = User()
