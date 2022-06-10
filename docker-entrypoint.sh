#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Apply fixtures
echo "Apply database fixtures"
python manage.py loaddata user/fixtures/department_data.json
python manage.py loaddata user/fixtures/major_data.json
python manage.py loaddata hy_act_server/fixtures/group_data.json
python manage.py loaddata user/fixtures/user_data.json
python manage.py loaddata program/fixtures/program_data.json


# Start Django app server
echo "Starting Django App server"
gunicorn hy_act_server.wsgi:application --bind unix:/run/gunicorn.sock -D

# Start nginx server
echo "Starting Nginx server"
nginx -g "daemon off;"
