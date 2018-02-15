FROM python:3

LABEL maintainer="Steve McQuaid <steve@stevemcquaid.com>"

LABEL version="1.0"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]