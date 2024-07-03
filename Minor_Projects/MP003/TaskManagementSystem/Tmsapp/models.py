from django.db import models

class TaskDetails(models.Model):
    task_name=models.CharField(max_length=200)
    task_status=models.BooleanField(default=False)
    

