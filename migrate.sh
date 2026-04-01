#!/bin/bash
set -e
PYTHON=/var/app/venv/staging-LQM1lest/bin/python
$PYTHON /var/app/staging/manage.py migrate --run-syncdb
$PYTHON /var/app/staging/manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    u = User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"
chmod 600 /var/app/staging/db.sqlite3
chown webapp:webapp /var/app/staging/db.sqlite3
