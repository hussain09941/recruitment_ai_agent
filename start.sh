#!/usr/bin/env bash
gunicorn --bind 0.0.0.0:$PORT recruitment_ai.wsgi:application