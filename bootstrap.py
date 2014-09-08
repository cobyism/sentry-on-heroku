import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "indexlogistics.settings.local")

from django.contrib.auth.models import User

SENTRY_ADMINS = os.environ.get('ADMINS', '').split(',')

for admin in SENTRY_ADMINS:
  User.objects.create_superuser(admin, admin, 'passworD1')
