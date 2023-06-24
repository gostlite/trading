#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt

# Run Django migrations
# python manage.py migrate

# Start the Django server
python manage.py runserver
