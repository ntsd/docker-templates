# Jenkins Template

#### Generate ssh keystore

``` bash
keytool -genkey -keyalg RSA -alias selfsigned -keystore jenkins_keystore.jks -storepass mypassword -keysize 4096
```

#### Get initial password

```
docker exec -it ${CONTAINER} cat /var/jenkins_home/secrets/initialAdminPassword
```

#### Reference

https://github.com/jenkinsci/docker

https://code-maze.com/ci-jenkins-docker/
