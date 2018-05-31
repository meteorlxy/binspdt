# binspdt - BINary Software Plagiarism Detection Tool

Still a work in progress

## Develop Guide

### Install the dependencies

```sh
pipenv install
yarn install
```

### Config Django

```sh
cp binspdt/settings.sample.py binspdt/settings.py 
```

Config `DATABASE` and `IDA` settings.

### Run migration

After config `DATABASE` correctly, migrate the database tables.

```sh
yarn migrate
```

### Build web client

Build the web client / develop the web client

```sh
yarn build # Build
yarn watch # Develop in watch mode
```

### Start Django dev server

```sh
yarn start
```
