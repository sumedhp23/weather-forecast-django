#!/usr/bin/env bash
exec gunicorn weather_project.wsgi:application
