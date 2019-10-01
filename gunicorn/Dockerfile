FROM python:3.6.4
MAINTAINER ntsd

# Software version management
ENV SUPERVISOR_VERSION=3.0r1-1+deb8u1
ENV GUNICORN_VERSION=19.7.1
ENV GEVENT_VERSION=1.2.2

# Environment setting
ENV APP_ENVIRONMENT production

# Flask demo application
COPY ./app /app
COPY ./wait-for-it.sh /app

RUN pip install -r /app/requirements.txt

# Gunicorn installation
RUN pip install gunicorn==$GUNICORN_VERSION gevent==$GEVENT_VERSION

# Gunicorn default configuration
COPY gunicorn.config.py /app/gunicorn.config.py

WORKDIR /app

RUN ["chmod", "+x", "./wait-for-it.sh"]

EXPOSE 80

CMD ["gunicorn", "run:app", "-c", "/app/gunicorn.config.py"]
