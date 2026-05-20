# Running the Django Web App (`money_manager_web/`)

This repo contains a desktop app (`money_manager/`) and a Django web app (`money_manager_web/`).

## Run locally (dev)

From the repo root:

```powershell
cd money_manager_web

# optional: create a .env file based on .env.example
Copy-Item .env.example .env

# Windows venv (already in this repo as .venv/)
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Open:
- `http://127.0.0.1:8000/` (redirects to login)
- `http://127.0.0.1:8000/admin/` (admin)

## Run “web” (production-like) locally

This uses `gunicorn` like a real deployment (still using your local `.env` + SQLite unless you set `DATABASE_URL`).

```powershell
cd money_manager_web
.\.venv\Scripts\python.exe manage.py collectstatic --noinput
.\.venv\Scripts\python.exe -m gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## Environment variables

Common vars are documented in `money_manager_web/.env.example`:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `TIME_ZONE`
- `DATABASE_URL` (optional, e.g. Postgres)

## Deploy

See `money_manager_web/DEPLOYMENT.md`.

