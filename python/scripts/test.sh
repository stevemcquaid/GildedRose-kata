#!/bin/bash
set -ex

docker run -it --rm --name zenrez -v "$PWD":/usr/src/myapp:Z -w /usr/src/myapp python:3 coverage make run main.py