#!/bin/bash
set -e
PYTHON=/var/app/venv/staging-LQM1lest/bin/python
$PYTHON /var/app/staging/manage.py migrate --run-syncdb
$PYTHON /var/app/staging/manage.py createsuperuser --noinput --username admin --email admin@example.com || true
chmod 664 /var/app/staging/db.sqlite3
chown webapp:webapp /var/app/staging/db.sqlite3
