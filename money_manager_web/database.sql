-- Expense Track PostgreSQL database provisioning script.
--
-- Run this with psql as a PostgreSQL administrator:
--   psql -U postgres -f database.sql
--
-- Before running, replace CHANGE_ME_STRONG_PASSWORD below.
-- This script creates the database and application login only.
-- Django migrations create and update the application tables:
--   .\.venv\Scripts\python.exe manage.py migrate

\set database_name 'expense_track'
\set app_user 'expense_track_app'
\set app_password 'CHANGE_ME_STRONG_PASSWORD'

SELECT format('CREATE ROLE %I LOGIN PASSWORD %L', :'app_user', :'app_password')
WHERE NOT EXISTS (
    SELECT 1
    FROM pg_roles
    WHERE rolname = :'app_user'
)
\gexec

SELECT format(
    'CREATE DATABASE %I OWNER %I ENCODING ''UTF8'' TEMPLATE template0',
    :'database_name',
    :'app_user'
)
WHERE NOT EXISTS (
    SELECT 1
    FROM pg_database
    WHERE datname = :'database_name'
)
\gexec

\connect :database_name

GRANT CONNECT ON DATABASE :"database_name" TO :"app_user";
GRANT USAGE, CREATE ON SCHEMA public TO :"app_user";
ALTER SCHEMA public OWNER TO :"app_user";

-- Put the same credentials in .env after provisioning:
-- DATABASE_URL=postgresql://expense_track_app:CHANGE_ME_STRONG_PASSWORD@localhost:5432/expense_track
-- URL-encode special characters in the password when building DATABASE_URL.
