#!/bin/sh

until cd /app/backend
do
    echo "Entering the app/backend folder..."
done


until python manage.py makemigrations
do
    echo "Making migrations..."
    sleep 2
done


until python manage.py migrate
do
    echo "Migrating..."
    sleep 2
done


python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput

gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000