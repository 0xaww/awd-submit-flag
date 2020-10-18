#!/bin/sh
docker build -t "env_test" .
docker run -d -p 9999:9999 8888:80 --name="env_test" env_test
