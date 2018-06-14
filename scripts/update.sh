#!/bin/bash
cd `dirname $0`/..

git pull origin master && pipenv install

if [ $? -eq 0 ]; then
  echo 'Done'
else
  echo 'Failed'
fi

echo 'exit in 3s...'
sleep 3
exit 0
