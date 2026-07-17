#!/bin/sh

echo "Waiting for database to be ready..."
while ! nc -z $DATABASE_HOST 5432; do
  sleep 1
done

python manage.py migrate

python manage.py runserver 0.0.0:8000
