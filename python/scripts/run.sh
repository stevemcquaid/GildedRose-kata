#!/bin/bash
set -ex

docker run -it --rm --name zenrez -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python main.py