from django.db import models
from django.conf import settings


class TaskResult(models.Model):
    task_name = models.CharField(max_length=20)
    task_result = models.TextField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
