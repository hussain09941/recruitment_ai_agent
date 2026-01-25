#!/usr/bin/env bash
. venv/bin/activate  # Use '.' instead of 'source' for POSIX shell compatibility
gunicorn --bind 0.0.0.0:$PORT recruitment_ai.wsgi:application