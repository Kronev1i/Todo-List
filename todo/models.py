from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done_or_not = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["done_or_not", "-created_at"]
