import os
import pexpect

username = os.environ.get('FIRST_USER_USERNAME')
email    = os.environ.get('FIRST_USER_EMAIL')
password = os.environ.get('FIRST_USER_PASSWORD')

child = pexpect.spawn ('sentry --config=sentry.conf.py createsuperuser')
child.expect ('Username:')
child.sendline (username)
child.expect ('Email address:')
child.sendline (email)
child.expect ('Password:')
child.sendline (password)
child.expect ('Password (again):')
child.sendline (password)
