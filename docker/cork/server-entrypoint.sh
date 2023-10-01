#!/bin/sh

until cd /app/cork
do
    echo "Entering the app/cork folder"
done

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py createsuperuser --noinput

gunicorn cork.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
# python manage.py runserver 0.0.0.0:8000