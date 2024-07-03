from django.contrib import admin
from .models import TaskDetails

@admin.register(TaskDetails)
class TaskDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'task_status')
