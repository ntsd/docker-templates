FROM jenkins/jenkins:alpine

# TODO use user "jenkins" instead
USER root

# Install docker
ENV DOCKER_VERSION=19.03.2
RUN cd /tmp  & \
    wget https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz && \
    tar xzvf docker-${DOCKER_VERSION}.tgz && \
    cp docker/docker /usr/local/bin/docker && \
    rm -rf docker*

# Install docker-compose
RUN apk add py-pip python3-dev libffi-dev openssl-dev gcc libc-dev make
RUN pip3 install docker-compose

# Copy keystore to jenkins
COPY jenkins_keystore.jks /var/lib/jenkins/

ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8443 --httpsKeyStore=/var/lib/jenkins/jenkins_keystore.jks --httpsKeyStorePassword=mypassword

EXPOSE 8443
