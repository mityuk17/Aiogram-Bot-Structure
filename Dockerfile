FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /project


COPY ./requirements.txt /project/requirements.txt
COPY ./.env /project/.env


RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt


COPY ./bot /project/bot
COPY ./.env /project/bot/.env