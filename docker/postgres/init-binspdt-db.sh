#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $BINSPDT_USER WITH PASSWORD $BINSPDT_PASSWORD;
  CREATE DATABASE binspdt_web;
  CREATE DATABASE binspdt_binary;
  GRANT ALL PRIVILEGES ON DATABASE binspdt_web TO $BINSPDT_USER;
  GRANT ALL PRIVILEGES ON DATABASE binspdt_binary TO $BINSPDT_USER;
EOSQL