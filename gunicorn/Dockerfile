FROM python:3.6.4

LABEL MAINTAINER="ntsd"

# Software version management
ENV SUPERVISOR_VERSION=3.0r1-1+deb8u1
ENV GUNICORN_VERSION=19.7.1
ENV GEVENT_VERSION=1.2.2

# Environment setting
ENV APP_ENVIRONMENT production

# Flask demo application
COPY ./app /app

# Install wait-for-it
COPY ./wait-for-it.sh /app
RUN chmod +x /app/wait-for-it.sh

# Install build-dependencies libffi-dev openssl-dev build-base
# RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base
# RUN pip install --upgrade pip

# Install requirements
RUN pip install -r /app/requirements.txt

# Gunicorn installation
RUN pip install gunicorn==$GUNICORN_VERSION gevent==$GEVENT_VERSION

# Gunicorn default configuration
COPY gunicorn.config.py /app/gunicorn.config.py

WORKDIR /app

EXPOSE 80

CMD ["gunicorn", "app:app", "-c", "/app/gunicorn.config.py"]
