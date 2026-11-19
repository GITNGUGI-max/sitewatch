# SiteWatch

A Python website monitoring application with a web dashboard, packaged using Docker Compose.

## Features

- Checks configured websites at a configurable interval.
- Records check results in `checks.log`.
- Displays the latest results on a web dashboard.
- Keeps saved results when containers are recreated.

## Services

- **worker:** Runs the website checks.
- **web:** Serves the Python dashboard using Gunicorn.
- **nginx:** Routes incoming requests to the dashboard.

## Requirements

Docker with Docker Compose. On Windows, start Docker Desktop and use Git Bash for the commands below.

## First-time setup

From the project directory:

```bash
cp .env.example .env
touch checks.log
docker compose up -d --build
```

The log file must exist before starting because it is mounted into the containers.

Open the dashboard at http://127.0.0.1:8080.

Edit `.env` to change the target URLs or check interval. Apply configuration changes with:

```bash
docker compose up -d
```

## Useful commands

Check service status:

```bash
docker compose ps
```

Follow the worker output:

```bash
docker compose logs -f worker
```

Read saved results:

```bash
tail -n 10 checks.log
```

Stop and remove the containers:

```bash
docker compose down
```

The `checks.log` file remains in the project directory.