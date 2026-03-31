#!/bin/bash
/var/app/venv/staging-LQM1lest/bin/python /var/app/staging/manage.py migrate --run-syncdb
/var/app/venv/staging-LQM1lest/bin/python /var/app/staging/manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
"
