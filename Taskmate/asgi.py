"""
ASGI config for Taskmate project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

import sys

sys.path.append('D:\\taskmate project\\taskmate\\Taskmate')  # Ensure the path is correct
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taskmate.settings')

application = get_asgi_application()
