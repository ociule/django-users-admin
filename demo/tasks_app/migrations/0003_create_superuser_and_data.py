from django.db import migrations
from django.conf import settings
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('djangoadmin')
    superuser.save()


def delete_superuser(apps, schema_editor):
    User.objects.filter(username="admin").delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks_app', '0002_create_users_and_group'),
    ]

    operations = [
        migrations.RunPython(create_superuser, delete_superuser),

        migrations.RunSQL("INSERT INTO tasks_app_tasklist (user_id, name, created_at) \
            SELECT auth_user.id, 'Alice''s Task List', CURRENT_TIMESTAMP FROM auth_user WHERE \
            auth_user.username = 'alice_non_staff';", "DELETE FROM tasks_app_tasklist"),

        migrations.RunSQL("INSERT INTO tasks_app_tasklist (user_id, name, created_at) \
            SELECT auth_user.id, 'Bob''s Task List', CURRENT_TIMESTAMP FROM auth_user WHERE \
            auth_user.username = 'bob_non_staff';", "DELETE FROM tasks_app_tasklist"),

        migrations.RunSQL("INSERT INTO tasks_app_task (list_id, name, created_at) VALUES (1, 'M1', CURRENT_TIMESTAMP);", "DELETE FROM tasks_app_task"),
        migrations.RunSQL("INSERT INTO tasks_app_task (list_id, name, created_at) VALUES (1, 'M2', CURRENT_TIMESTAMP);", "DELETE FROM tasks_app_task"),
        migrations.RunSQL("INSERT INTO tasks_app_task (list_id, name, created_at) VALUES (1, 'M3', CURRENT_TIMESTAMP);", "DELETE FROM tasks_app_task"),
        migrations.RunSQL("INSERT INTO tasks_app_task (list_id, name, created_at) VALUES (1, 'D1', CURRENT_TIMESTAMP);", "DELETE FROM tasks_app_task"),
        migrations.RunSQL("INSERT INTO tasks_app_task (list_id, name, created_at) VALUES (1, 'D2', CURRENT_TIMESTAMP);", "DELETE FROM tasks_app_task"),
        migrations.RunSQL("INSERT INTO tasks_app_task (list_id, name, created_at) VALUES (1, 'R1', CURRENT_TIMESTAMP);", "DELETE FROM tasks_app_task"),
    ]
