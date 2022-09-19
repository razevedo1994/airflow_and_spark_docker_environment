#!/bin/bash

# Build the base images from which are based the Dockerfiles
# then Startup all the containers at once
docker-compose up airflow-init && \
docker-compose up -d
