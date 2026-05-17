Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (git rev-parse --show-toplevel)
$webDir = Join-Path $repoRoot "money_manager_web"

Set-Location $webDir

if (-not (Test-Path ".\\.venv\\Scripts\\python.exe")) {
  throw "Missing .venv. Create it first in money_manager_web/."
}

if (-not (Test-Path ".env") -and (Test-Path ".env.example")) {
  Copy-Item ".env.example" ".env"
}

.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py collectstatic --noinput
.\.venv\Scripts\python.exe -m gunicorn config.wsgi:application --bind 0.0.0.0:8000

