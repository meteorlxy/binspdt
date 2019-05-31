# BinSPDT

> Binary Software Plagiarism Detection Tool

## Develop Guide

### Install the dependencies

```sh
pipenv install
npm install
```

### Config Environment Variables

```sh
cp .env.example .env
```

Config database, IDA Pro and other settings in `.env` file.

### Run migration

After config PostgreSQL correctly, migrate the database tables.

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
- IDA Pro 7.0+ => binexport 10
