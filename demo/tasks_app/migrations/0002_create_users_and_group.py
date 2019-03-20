from django.db import migrations
from django.conf import settings
from django.contrib.auth.models import User, Group, Permission

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version

    perms_str = [
    "Can view task tag",
    "Can view task list",
    "Can change task list",
    "Can add task list",
    "Can delete task list",
    "Can view task",
    "Can change task",
    "Can add task",
    "Can delete task",
    ]

    perms = Permission.objects.filter(name__in=perms_str)

    if len(perms) != len(perms_str):
        raise ValueError(f"Expected 9 permissions, got {len(perms)}")

    g = Group.objects.create(name='non_staff')
    g.permissions.set(perms)
    g.save()

    u1 = User.objects.create_user('alice_non_staff', '', 'useruser')
    u2 = User.objects.create_user('bob_non_staff', '', 'useruser')
    u1.groups.add(g)
    u2.groups.add(g)
    u1.save()
    u2.save()


def reverse_func(apps, schema_editor):

    User.objects.filter(username="alice_non_staff").delete()
    User.objects.filter(username="bob_non_staff").delete()

    Group.objects.filter(name="non_staff").delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
