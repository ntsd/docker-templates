FROM jenkins/jenkins:alpine

USER jenkins

COPY jenkins_keystore.jks /var/lib/jenkins/

ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8443 --httpsKeyStore=/var/lib/jenkins/jenkins_keystore.jks --httpsKeyStorePassword=mypassword
EXPOSE 8443
