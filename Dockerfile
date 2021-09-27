FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /django-tech-test

COPY requirements.txt /django-tech-test/

RUN pip3 install -r requirements.txt
COPY . /django-tech-test/