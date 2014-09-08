import sentry.conf.py
from django.contrib.auth.models import User
SENTRY_KEY = os.environ.get('SENTRY_KEY')
SENTRY_ADMINS = os.environ.get('ADMINS', '').split(',')
for admin in SENTRY_ADMINS:
  User.objects.create_superuser(admin, admin, 'passworD1')
