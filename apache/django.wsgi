import os
import sys

path = '/home/coacha'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'coacha.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
