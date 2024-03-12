#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=SEAY.settings.prod

echo 'Applying migrations...'
python manage.py migrate --settings=SEAY.settings.prod

echo 'Running server...'
python manage.py runserver --settings=SEAY.settings.prod
