#!/usr/bin/env bash
source venv/bin/activate  # Activate Render's virtual environment
gunicorn --bind 0.0.0.0:$PORT recruitment_ai.wsgi:application