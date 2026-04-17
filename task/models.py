from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=200)

    def __str__(self):
        # gives a human readable method in python
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank = True)

    class TaskStatus(models.TextChoices):
        COMPLETED = "CO", "Completed"
        PENDING = "PE", "Pending"
        DROPPED = "DR", "Dropped"

    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2,
    )

    def __str__(self):
        return f'{self.content} - {self.status}'     