# Jenkins Template

## Create Volume

``` bash
docker volume create docker-bin --opt device=/snap/bin/docker --opt type=bind
```

## Generate ssh keystore

``` bash
keytool -genkey -keyalg RSA -alias selfsigned -keystore jenkins_keystore.jks -storepass mypassword -keysize 4096
```

## Get initial password

``` bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Fix permission denined

``` bash
sudo chown -R 1000 jenkins_data
```

## Reference

https://github.com/jenkinsci/docker

https://code-maze.com/ci-jenkins-docker/

https://github.com/hughperkins/howto-jenkins-ssl/blob/master/letsencrypt.md
