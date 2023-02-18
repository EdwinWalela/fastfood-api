#!/usr/bin/env sh

# Adapted from https://itnext.io/full-production-django-docker-configuration-75824855da03
python3 manage.py migrate --noinput
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

# Getting static files for Admin panel hosting
python3 manage.py collectstatic --noinput

python3 manage.py qcluster &

uwsgi --http "0.0.0.0:${PORT}" --single-interpreter --module configurations.wsgi --master --processes 4 --threads 2