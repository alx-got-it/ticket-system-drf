#!/bin/sh

#until cd /app
#do
#    echo "Entering the app folder"
#done
#
#python source venv/bin/activate

until cd /app/cork
do
    echo "Entering the app/cork folder"
done

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

gunicorn cork.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
# python manage.py runserver 0.0.0.0:8000
