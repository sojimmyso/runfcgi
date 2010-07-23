#!/usr/bin/env python

from distutils.core import setup

setup(
        name='runfcgi',
        version='1.0',
        description='Shortcut to standard django manage.py command to run fastcgi process',
        author='Andrey Bulgakov',
        author_email='mail@andreiko.ru',
        url='http://github.com/andreiko/runfcgi',
        packages=['runfcgi', 'runfcgi.management', 'runfcgi.management.commands'],
    )
