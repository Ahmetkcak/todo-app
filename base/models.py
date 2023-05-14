
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TaskList(models.Model):
    id = models.AutoField(primary_key=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField
    deletedDate = models.DateTimeField
    completionPercentage = models.IntegerField

    def save(self, *args, **kwargs):
        self.updatedDate = timezone.now()
        super(TaskList, self).save(*args, **kwargs)



class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    taskListId = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField
    deletedDate = models.DateTimeField
    description = models.TextField(null=False,blank=False)
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updatedDate = timezone.now()
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['completed']