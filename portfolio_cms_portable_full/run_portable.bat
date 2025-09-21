@echo off
setlocal
cd /d "%~dp0"

if not exist .venv (
  py -m venv .venv
)
call .\.venv\Scripts\activate.bat

pip install -r requirements.txt

IF EXIST db.sqlite3 (
  echo Using existing db.sqlite3 (seeded).
) ELSE (
  echo Creating database...
  python manage.py makemigrations projects --noinput
  python manage.py migrate --noinput
)

start "" http://127.0.0.1:8000/
python manage.py runserver