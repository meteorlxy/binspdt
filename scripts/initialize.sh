#!/bin/bash

cd `dirname $0`/..

echo 'Installing and migrating...'

pipenv install && \
pipenv run migrate && \
pipenv run migrate-binary && \
npm install && \
npm run build

if [ $? -eq 0 ]; then
  echo 'Done'
else
  echo 'Failed'
fi

echo 'exit in 3s...'
sleep 3
exit 0
