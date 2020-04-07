#!/usr/bin/env bash

docker-compose stop

docker-compose rm -f

docker-compose up -d

export container=$(docker ps -aqf "name=secure")

docker exec $container sh /scripts/keycloak-setup.sh