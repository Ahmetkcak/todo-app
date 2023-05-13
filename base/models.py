from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdDate = models.DateTimeField
    updatedDate = models.DateTimeField
    deletedDate = models.DateTimeField
    completionPercentage = models.IntegerField



class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    taskListId = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField
    deletedDate = models.DateTimeField
    description = models.TextField(null=False,blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['completed']