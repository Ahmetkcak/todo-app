from asyncio import Task

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone


class TaskList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    createdDate = models.DateTimeField
    updatedDate = models.DateTimeField
    deletedDate = models.DateTimeField
    completionPercentage = models.IntegerField

    def save(self, *args, **kwargs):
        self.updatedDate = timezone.now()
        super(TaskList, self).save(*args, **kwargs)

    @receiver(pre_delete, sender=Task)
    def update_deleted_date(sender, instance, **kwargs):
        instance.deletedDate = timezone.now()
        instance.save()



class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskListId = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField
    deletedDate = models.DateTimeField
    description = models.TextField(null=False,blank=False)
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updatedDate = timezone.now()
        super(Task, self).save(*args, **kwargs)

    @receiver(pre_delete, sender=Task)
    def update_deleted_date(sender, instance, **kwargs):
        instance.deletedDate = timezone.now()
        instance.save()

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['completed']