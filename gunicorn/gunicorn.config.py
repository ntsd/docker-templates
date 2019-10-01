  
"""Gunicorn configuration."""
import os
# https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
# http://docs.gunicorn.org/en/0.17.2/configure.html

bind = '0.0.0.0:80'

workers = 4
worker_class = 'gevent'

accesslog = '-'

timeout = os.getenv('GUNICORN_TIMEOUT', 300) # defult 5 minutes
