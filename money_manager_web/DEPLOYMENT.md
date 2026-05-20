# Deployment (Django + PostgreSQL)

## 1) Environment variables

Copy `.env.example` to `.env` for local dev, or set these in your hosting provider:

- `SECRET_KEY` (required in production)
- `DEBUG` (`False` in production)
- `ALLOWED_HOSTS` (comma-separated, e.g. `example.com,www.example.com`)
- `DATABASE_URL` (PostgreSQL recommended; example: `postgres://USER:PASSWORD@HOST:5432/DBNAME`)

Optional (password reset email):

- `EMAIL_BACKEND` (default is console backend)
- `DEFAULT_FROM_EMAIL`
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`

## 2) Install dependencies

`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

## 3) Migrate database

`.\.venv\Scripts\python.exe manage.py migrate`

## 4) Create admin user

`.\.venv\Scripts\python.exe manage.py createsuperuser`

## 5) Static files

For most hosts:

`.\.venv\Scripts\python.exe manage.py collectstatic --noinput`

## 6) Run in production

Gunicorn command (also in `Procfile`):

`gunicorn config.wsgi:application`

