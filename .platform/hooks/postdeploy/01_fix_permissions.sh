#!/bin/bash
if [ -f /var/app/current/db.sqlite3 ]; then
    chown webapp:webapp /var/app/current/db.sqlite3
    chmod 664 /var/app/current/db.sqlite3
fi
