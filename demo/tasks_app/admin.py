from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import TaskTag, TaskList, Task


@admin.register(Task)
class TaskAdmin(GuardedModelAdmin):
    autocomplete_fields = ('tags', )


@admin.register(TaskTag)
class TaskTagAdmin(GuardedModelAdmin):
    search_fields = ('tag', )

class TaskInline(admin.TabularInline):
    model = Task
    autocomplete_fields = ('tags', )

@admin.register(TaskList)
class TaskListAdmin(GuardedModelAdmin):
    search_fields = ('name',)

    list_display = ('name', 'user')

    inlines = [
        TaskInline,
    ]
