from django.contrib import admin
from .models import Job, Task

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_id', 'created_at',  'coins']
    readonly_fields = ['job_id', 'created_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['coin_name', 'job_id', 'price', 'price_change', 'market_cap', 'market_cap_rank', 'volume', 'volume_rank', 'volume_change', 'circulating_supply', 'total_supply', 'diluted_market_cap', 'created_at']
    list_filter = ['job_id']  # Add 'job_id' to list_filter
    readonly_fields = ['created_at']

    # If you prefer to keep the 'Job ID' header, you can specify it directly in list_display
    list_display_links = ['coin_name', 'job_id']
    
