FROM python:3.8.12-alpine3.15
MAINTAINER Diego Escobar <diegoe@checkpoint.com>

ARG PYPI_URL='https://pypi.org/'

RUN apk add --update --no-cache bash ncurses python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade \
    --index $PYPI_URL/pypi --index-url $PYPI_URL/simple \
    --trusted-host $(echo $PYPI_URL | awk -F[/:] '{print $4}') \
    pip setuptools boto boto3 netaddr simplejson simple-term-menu bs4 requests

RUN mkdir -pv /tmp/webinar/

WORKDIR  /tmp/webinar

COPY zero_touch_function.py import.json importgaiatemplate.json ./

RUN chmod +x zero_touch_function.py

ENTRYPOINT ["python3", "/tmp/webinar/zero_touch_function.py"]
