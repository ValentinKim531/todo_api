#!/bin/sh

echo "⏳ Ожидаем PostgreSQL на $DB_HOST:5432..."
while ! python -c "
import socket
import time
try:
    with socket.create_connection((\"$DB_HOST\", 5432), timeout=1):
        pass
except OSError:
    raise SystemExit(1)
"; do
  sleep 1
done

echo "База доступна"

echo "Применяем миграции..."
python manage.py migrate

echo "Загружаем фикстуры..."
python manage.py loaddata fixtures/initial_fixtures.json || echo "Нет фикстур"

echo "Запускаем сервер..."
python manage.py runserver 0.0.0.0:8000
