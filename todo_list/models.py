from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=65, unique=True)
