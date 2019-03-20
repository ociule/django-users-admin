from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User

from guardian.admin import GuardedModelAdmin
from users_admin import UsersAdminBase

from .models import TaskTag, Task, TaskList


class UsersAdmin(UsersAdminBase):
    site_header = "Users' admin demo"
    site_title = "Users' admin demo"
    login_template = 'users_admin_login.html'

users_admin_site = UsersAdmin()


class TaskInline(admin.TabularInline):
    model = Task
    autocomplete_fields = ('tags', )
    template = 'edit_inline_tabular.html'


@admin.register(TaskList, site=users_admin_site)
class TaskListAdmin(GuardedModelAdmin):
    include_object_permissions_urls = False
    user_can_access_owned_objects_only = True

    search_fields = ('name',)

    inlines = [TaskInline,]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ We restrict user choices to the logged in user only """
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(id=request.user.id).all()
            kwargs["empty_label"] = None
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(TaskTag, site=users_admin_site)
class TaskTagAdmin(GuardedModelAdmin):
    include_object_permissions_urls = False

    search_fields = ('tag', )
