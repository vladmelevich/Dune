#!/bin/sh

# Создаем директорию для логов, если ее нет
mkdir -p /app/logs

# Применяем миграции базы данных
python manage.py migrate --noinput

# Собираем статические файлы
python manage.py collectstatic --noinput

# Создаем суперпользователя, если необходимо
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'email@mail.ru', '12133')
END

# Запускаем сервер
exec gunicorn --bind 0.0.0.0:3200 dune.wsgi:application

