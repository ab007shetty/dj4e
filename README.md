DJ4E Coursera
=============

This is a Complete files of the Course django for everybody.

Running Locally
---------------

If you have Django installed on your local computer you can test any of the sample
applications by going into the folder and starting the server:

    cd dj4e
    python3 manage.py runserver

And visit `http://localhost:8000`.

Running on PythonAnywhere
-------------------------

Once you have checked out the code under `django_projects`, and
ran the migrations and load scripts,
go under the Web tab, update the config files to point to your new application:

    Source code:                /home/--your-account--/django_projects/dj4e
    Working Directory:          /home/--your-account--/django_projects/dj4e

Use this as your `WGSI configuration file`:

    import os
    import sys

    path = os.path.expanduser('~/django_projects/dj4e')
    if path not in sys.path:
        sys.path.insert(0, path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'dj4e.settings'
    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())

You can edit these files and settings in the Web tab to switch between
your various projects on PythonAnywhere.  Make sure to reload under the Web tab after
every file or configuration change.



