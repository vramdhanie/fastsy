#!/bin/sh
python ./app/backend_pre_start.py
alembic upgrade head
python ./app/initial_data.py