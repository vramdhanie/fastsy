#!/bin/sh
export PYTHONPATH=$PYTHONPATH:.
python ./app/backend_pre_start.py
alembic upgrade head
python ./app/initial_data.py