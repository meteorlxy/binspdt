#!/bin/bash

cd `dirname $0`/..

cd server

pipenv run celery -A binspdt worker -l INFO -P eventlet
