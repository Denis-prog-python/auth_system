"""
WSGI config for auth_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_system.settings')

# Получите WSGI-приложение
application = get_wsgi_application()