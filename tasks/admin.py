from django.contrib import admin
from tasks.models import ToDoItem


@admin.register(ToDoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("description", "is_completed", "created")
