from django.db import models
from django.contrib.auth.models import User


class TaskTag(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.tag


class TaskList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='My Task List')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(TaskTag, blank=True)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.name}"
