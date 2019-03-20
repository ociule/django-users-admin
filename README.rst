
Users' admin
#############

Try the demo here: https://users-admin.herokuapp.com

The Django admin app is very popular for creating data-centric CRUD interfaces, and this
can be done quickly and with barely any effort. The admin is very customizable and useful.

The users_admin package gives you the power to build user-accessible interfaces using the admin app.
Just register a model with the users_admin_site object, just like you would register it with the admin site,
and a CRUD interface will be created for it.

You can customise this users' admin just as you can `customise the admin app <https://docs.djangoproject.com/en/stable/ref/contrib/admin/#adminsite-objects>`_.

The Django admin site (available on /admin) continues to work as usual. Users' admin does not interfere with it.

Compatibility
==============

Users_admin has been tested on Django 2.1 and Python 3.7, but it should work with any Django >= 2.0 and Python >= 3.6

How to use
===========

Have a look at how users_admin is used inside the demo: first look at `demo/tasks_app/users_admin.py <demo/tasks_app/users_admin.py>`_

We define a custom users_admin_site instance based on users_admin.UsersAdminBase. We can customize this instance
however we wish.

Then, in the project `urls.py <demo/demo/urls.py>`_, we add our new users_admin_site urls
just like we add the classic admin URLs:

.. code:: python

  from tasks_app.users_admin import users_admin_site

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', users_admin_site.urls),
  ]

Now, back to `users_admin.py <demo/tasks_app/users_admin.py>`_ we can add the
models for which we want the CRUD interface:

.. code:: python

  users_admin_site.register(MyModel)

  # or we can register a custom ModelAdmin

  @admin.register(MyModel, site=users_admin_site)
  class MyModelAdmin(admin.ModelAdmin):
    pass

User's permissions
===================

Permissions work in users' admin just like in the normal admin. Superusers can do anything. The rest must be given
permission to view, add, change or delete any model. You must assign permissions to your users, otherwise they won't be able
to do anything.

Customization
==============

Users' admin can be customized `like the classic admin can be <https://docs.djangoproject.com/en/stable/ref/contrib/admin/>`_.

The tasks app of the demo project shows how to use a custom users_admin_site, custom ModelAdmins,
custom model templates and admin-wide custom templates. They also customise search_fields and autocomplete_fields.

The demo also uses django-guardian to implement per row permissions. Users can only see their own task lists.
This is implemented simply by having a user field on TaskList, having TaskListAdmin inherit from GuardedModelAdmin with
user_can_access_owned_objects_only set to True.

A multi-tenant app with organizations could be implemented easily by using user_can_access_owned_by_group_objects_only and creating a Group per organization.

The demo shows how a third-party tool (django-guardian) meant to work with the classic admin can be used for users' admin.

Demo
=====

Inside the demo dir you'll find a django project that uses users_admin.
Check it out online at https://users-admin.herokuapp.com/

Note that the alice and bob users are not staff and can't connect to the classic admin interface. But they can use the users' admin interface.

Thanks
=======

Thanks to Tryolabs for the inspiration.
See https://tryolabs.com/blog/2012/06/18/django-administration-interface-for-non-staff-users/

License
========

BSD 3 clause
