#!/usr/bin/env bash

#starts up all database and system architecture Docker containers

docker-compose -f ./lattice_system_architecture/docker-compose.yml up -d
docker-compose -f ./lattice_databases/docker-compose.yml up -d