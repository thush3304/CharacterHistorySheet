#!/bin/bash

set -e

#Build
docker-compose build --parrallel

#Push 
docker login -u ${DOCKERHUB_USR} -p ${DOCKERHUB_PSW}
docker-compose push