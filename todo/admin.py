from django.contrib import admin
from .models import task

@admin.register(task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'desc')
