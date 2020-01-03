FROM python:3.6

WORKDIR app
COPY requirements.txt /app

RUN apt-get update && apt-get upgrade 
RUN pip install -r requirements.txt
