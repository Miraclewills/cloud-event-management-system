#!/bin/bash
set -e
PYTHON=/var/app/venv/staging-LQM1lest/bin/python
$PYTHON /var/app/staging/manage.py migrate --run-syncdb
$PYTHON /var/app/staging/manage.py shell << 'PYEOF'
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
    print("Superuser created")
else:
    print("Superuser already exists")
PYEOF
