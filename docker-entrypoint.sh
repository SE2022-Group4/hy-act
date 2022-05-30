#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start Django app server
echo "Starting Django App server"
gunicorn hy_act_server.wsgi:application --bind unix:/run/gunicorn.sock -D

# Start nginx server
echo "Starting Nginx server"
nginx -g "daemon off;"
