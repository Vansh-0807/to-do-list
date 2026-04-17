from django.contrib import admin
from django.utils import timezone
from . import models
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = [
            ('content', 'deadline'),
            'tags'
        ]
    
    list_display = ['content', 'status'] #it will create resp attributes mentioned in the list_display
    list_editable = ['status'] #it will allow to edit only those attributes which are present in the list_editable
    actions = ['mark_complete', 'mark_pending']
    list_filter = ['status'] #creates a sidebar showing the status of each Tasks
    search_field = ['content'] #allows searching by task content

    def mark_complete(model_admin, request, queryset): #model_admin is used to access the admin models
        queryset.update(
            status = models.Task.TaskStatus.COMPLETED,
            completed_at = timezone.now(),
        )
    mark_complete.short_description = "Mark these tasks as completed. "

    def mark_pending(model_admin, request, queryset):
        queryset.update(
            status = models.Task.TaskStatus.PENDING,
            completed_at = None,
        )
    mark_pending.short_description = "Mark these tasks as pending."

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_field = ['name'] 
# admin.site.register(models.Task, TaskAdmin)
# admin.site.register(models.Tag)

