# Deployment (Django + PostgreSQL)

## Database choice for multiple users

Use one PostgreSQL database as the application's shared production database. Django stores user accounts, login sessions, budgets, goals, and transactions there, and the application restricts each finance record to its owning user.

The project already includes the PostgreSQL driver (`psycopg`) and reads its connection from `DATABASE_URL`. SQLite is suitable for local development, but it should not be used as the deployed multi-user database.

## Creating your own PostgreSQL database

For a PostgreSQL server that you administer:

1. Edit `database.sql` and replace `CHANGE_ME_STRONG_PASSWORD`.
2. Run the provisioning script as a PostgreSQL administrator:

   `psql -U postgres -f database.sql`

3. Add a matching connection URL to `.env` as `DATABASE_URL`. URL-encode special characters used in the password.
4. Run `.\.venv\Scripts\python.exe manage.py migrate` to create Django's application tables.

For a hosted PostgreSQL provider, it usually creates the database and username for you. In that case, do not run `database.sql`; set the provider's connection URL as `DATABASE_URL` and run migrations.

## 1) Environment variables

Copy `.env.example` to `.env` for local dev, or set these in your hosting provider:

- `SECRET_KEY` (required in production)
- `DEBUG` (`False` in production)
- `ALLOWED_HOSTS` (comma-separated, e.g. `example.com,www.example.com`)
- `DATABASE_URL` (required for production; example: `postgresql://USER:PASSWORD@HOST:5432/DBNAME?sslmode=require`)

Optional (password reset email):

- `EMAIL_BACKEND` (default is console backend)
- `DEFAULT_FROM_EMAIL`
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`

## 2) Install dependencies

`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

## 3) Migrate database

`.\.venv\Scripts\python.exe manage.py migrate`

This creates Django's user/login tables and the expense tables in the configured PostgreSQL database.

## 4) Create admin user

`.\.venv\Scripts\python.exe manage.py createsuperuser`

## 5) Static files

For most hosts:

`.\.venv\Scripts\python.exe manage.py collectstatic --noinput`

## 6) Run in production

Gunicorn command (also in `Procfile`):

`gunicorn config.wsgi:application`

## Moving existing SQLite data to PostgreSQL

If `db.sqlite3` already contains accounts or expenses that must be retained:

1. Make a backup of `db.sqlite3`.
2. With SQLite still configured, export the data:

   `.\.venv\Scripts\python.exe manage.py dumpdata --exclude contenttypes --exclude auth.permission --indent 2 > sqlite-data.json`

3. Set `DATABASE_URL` to the PostgreSQL connection URL.
4. Create the PostgreSQL schema:

   `.\.venv\Scripts\python.exe manage.py migrate`

5. Import the exported users and expense records:

   `.\.venv\Scripts\python.exe manage.py loaddata sqlite-data.json`

## What about MySQL?

Django supports MySQL, but this project is already configured and packaged for PostgreSQL. PostgreSQL is the recommended production choice here; use MySQL only when your hosting environment specifically requires it, because switching would require a MySQL driver and a separate migration/testing pass.

## Design diagrams

PlantUML design documentation is stored in `docs/uml/`:

- `auth-sequence.puml`
- `use-case.puml`
- `system-diagram.puml`
- `database-schema.puml`

See `docs/uml/README.md` for rendering instructions.
