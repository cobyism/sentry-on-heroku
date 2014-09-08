# [Sentry](https://getsentry.com) on Heroku

Sentry is a realtime, platform-agnostic error logging and aggregation platform.

To get your own instance of Sentry running on Heroku, just click the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cobyism/sentry-on-heroku)

## Follow-up

Unfortunately, there’s one step you have to do manually via the command-line
before you can use your Sentry installation. First, ensure you have the
[Heroku Toolbelt](https://toolbelt.heroku.com/) installed, and then run the following:

```sh
heroku run --app YOURAPPNAME sentry --config=sentry.conf.py createsuperuser
```

Enter a username, email address, and password for your first user account.

## License

Please refer to [the license](https://github.com/getsentry/sentry/blob/master/LICENSE)
on the main Sentry repository.
