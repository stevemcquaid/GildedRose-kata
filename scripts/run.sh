#!/bin/bash
set -ex

docker run -it --rm --name zenrez-node -v "$PWD":/usr/src/myapp -w /usr/src/myapp node:6 npm start