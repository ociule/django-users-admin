release: cd demo && DJANGO_SETTINGS_MODULE=demo.settings_heroku python manage.py migrate
web: cd demo && gunicorn demo.wsgi:application
