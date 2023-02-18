# syntax=docker/dockerfile:1.4
FROM  python:3.7-slim
EXPOSE 8000
WORKDIR /app 
COPY api/requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app 


RUN apt update && apt install gcc -y
RUN pip install uwsgi

COPY runner.sh /code/

ENV UWSGI_STATIC_MAP="/static/=/code/static/"
ENV UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|yml) 315360000"

CMD ["bash" ,"/code/runner.sh"]
