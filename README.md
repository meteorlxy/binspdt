# binspdt

> BINary Software Plagiarism Detection Tool

Still a work in progress

## Develop Guide

### Install the dependencies

```sh
pipenv install
npm run install
```

### Config Django

```sh
cp server/binspdt/settings.sample.py server/binspdt/settings.py 
```

Config `DATABASE` and `IDA` settings.

### Run migration

After config `DATABASE` correctly, migrate the database tables.

```sh
npm run migrate
```

### Build web client

Build the web client / develop the web client

```sh
npm run build # Build
npm run dev # Develop in watch mode
```

### Start Django dev server

```sh
npm run start
```

## Notice

You should have [IDA Pro](https://www.hex-rays.com/products/ida/) and corresponding version of [binexport](https://github.com/google/binexport) on your machine.

- IDA Pro 6.8 => binexport 8
- IDA Pro 6.95 => binexport 9
- IDA Pro 7.0 => binexport 10
