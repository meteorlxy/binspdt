#!/bin/bash

cd `dirname $0`/..

settings_sample_file='server/binspdt/settings.sample.py'
settings_file='server/binspdt/settings.py'

if [ -f $settings_sample_file ] && [ ! -f $settings_file ]; then
  echo 'Copy the sample settings file...'
  cp server/binspdt/settings.sample.py server/binspdt/settings.py
fi

echo 'Installing and migrating...'
# docker exec postgres createdb -Upostgres binspdt_web
# docker exec postgres createdb -Upostgres binspdt_binary
pipenv install && \
pipenv run migrate && \
pipenv run migrate-binary

if [ $? -eq 0 ]; then
  echo 'Done'
else
  echo 'Failed'
fi

echo 'exit in 3s...'
sleep 3
exit 0
