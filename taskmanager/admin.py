from django.contrib import admin
from .models import Job, Task

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_id', 'created_at']
    readonly_fields = ['job_id', 'created_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['coin_name', 'job', 'created_at']
    list_filter = ['job']
    readonly_fields = ['created_at']
