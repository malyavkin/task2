from django.db import models
from django.conf import settings


class TaskResult(models.Model):
    task_name = models.CharField(max_length=20, choices=(
        ('nth_prime', 'Nth prime'),
        ('factorize', 'Factorize'),
        ('ping', 'Ping'),
    ))
    args = models.TextField(max_length=4096, default="")
    task_result = models.TextField(max_length=4096, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
