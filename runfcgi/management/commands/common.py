import subprocess
import os
import time
import signal
from django.conf import settings
from django.core.servers import fastcgi

def get_options():
    try:
        options = settings.FASTCGI_OPTIONS
    except AttributeError:
        options = {}
    return options

def get_pidfile():
    return get_options().get('pidfile', settings.DJANGO_ROOT + 'var/run/fastcgi.pid')

def get_workdir():
    return get_options().get('workdir', settings.DJANGO_ROOT)

def get_socket():
    return get_options().get('socket', settings.DJANGO_ROOT + 'var/run/fastcgi.socket')

def get_umask():
    return get_options().get('umask', '000')

def is_running():
    pidfile = get_pidfile()
    if os.path.exists(pidfile):
        try:
            f = open(pidfile, 'r')
            pid = int(f.read())
            f.close()
        except (IOError, ValueError):
            return False
        try:
            os.kill(pid, 0)
            return pid
        except OSError:
            return False
    else:
        return False

def start():
    options = get_options()
    options['pidfile'] = get_pidfile()
    options['workdir'] = get_workdir()
    if 'host' not in options or 'port' not in options:
        options['socket'] = get_socket()
        options.pop('host', None)
        options.pop('port', None)
    else:
        options.pop('socket', None)

    options['umask'] = get_umask()
    fastcgi.runfastcgi(**options)

def stop():
    pid = is_running()
    if pid:
        os.kill(pid, signal.SIGTERM)
        try:
            while os.kill(pid,0):
                time.sleep(0.1)
        except OSError:
            pass
        for filename in (get_pidfile(), get_socket()):
            try:
                os.unlink(filename)
            except OSError:
                pass

