#!/bin/sh

until cd /app/cork
do
    echo "Waiting for server volume"
done

# run a worker :)
celery -A cork worker --loglevel=info --concurrency 1 -E