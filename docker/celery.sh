#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    alembic current
    celery -A src.tasks.tasks:celery worker --loglevel=INFO
elif [[ "${1}" == "flower" ]]; then
    celery -A src.tasks.tasks:celery flower
fi
