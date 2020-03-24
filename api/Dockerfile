FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# docker exec -it api bash
# django-admin startproject ファイル名 .
# 設定 settings.py ALLOWED_HOSTS = ["localhost"]
# python manage.py startapp ファイル名
# python manage.py makemigrations 
# python manage.py migrate
