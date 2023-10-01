#!/bin/sh

until cd /app/cork
do
    echo "Entering the app/cork folder"
done


until python manage.py makemigrations
do
    echo "Making migrations"
    sleep 2
done


until python manage.py migrate
do
    echo "Migrating"
    sleep 2
done


untilpython manage.py collectstatic --noinput
do
    echo "Collecting static"
    sleep 2
done

# python manage.py createsuperuser --noinput

gunicorn cork.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
# python manage.py runserver 0.0.0.0:8000