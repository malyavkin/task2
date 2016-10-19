from django.db import models
from django.conf import settings


class TaskResult(models.Model):
    task_name = models.CharField(max_length=20)
    args = models.TextField(max_length=4096)
    task_result = models.TextField(max_length=4096)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
