FROM jenkins/jenkins:alpine

# TODO use user "jenkins" instead
USER root

RUN apk add py-pip python3-dev libffi-dev openssl-dev gcc libc-dev make

RUN pip3 install docker-compose

COPY jenkins_keystore.jks /var/lib/jenkins/

ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8443 --httpsKeyStore=/var/lib/jenkins/jenkins_keystore.jks --httpsKeyStorePassword=mypassword
EXPOSE 8443
