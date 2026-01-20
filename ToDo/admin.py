from django.contrib import admin

# importing models
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'completed_yes_no']

    # function to display yes/no 
    def completed_yes_no(self, obj):
        if obj.completed:
            return "Yes"
        else:
            return "No"
admin.site.register(Task, TaskAdmin)
