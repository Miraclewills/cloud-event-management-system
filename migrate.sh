#!/bin/bash
set -e
PYTHON=$(find /var/app/venv -name "python3.9" -type f | head -1)
$PYTHON /var/app/staging/manage.py migrate --run-syncdb
$PYTHON /var/app/staging/manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
    print('Superuser created')
else:
    print('Superuser already exists')
"
