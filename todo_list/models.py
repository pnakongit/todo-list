from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to="todo_list.Tag",
        related_name="tags",
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.content}"


class Tag(models.Model):
    name = models.CharField(max_length=65, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
