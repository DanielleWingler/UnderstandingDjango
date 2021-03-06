"""
WSGI config for TestSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/

There should be a .pyc file by the same name at creation.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestSite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
