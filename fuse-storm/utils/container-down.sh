#!/bin/sh
echo shutting down docker container
docker stop $(docker ps -q)