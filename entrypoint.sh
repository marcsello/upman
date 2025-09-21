#!/bin/sh

echo "Starting upman backend server..."

python3 init.py # <- single-threaded init stuff

# run the app in a multi-worker multi-thread env
exec gunicorn -b 0.0.0.0:8080 --workers 4 --threads 2 'application:create_app()'
