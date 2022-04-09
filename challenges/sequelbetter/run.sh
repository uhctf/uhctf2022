#!/bin/sh
FLASK_ENV=release
cd webserver
source venv/bin/activate
gunicorn app -b :80