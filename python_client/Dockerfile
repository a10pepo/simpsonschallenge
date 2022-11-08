FROM python:3.9.15-slim-buster


RUN apt-get update
RUN mkdir /datafolder


WORKDIR /datafolder
COPY main.py /datafolder
COPY requirements.txt /datafolder
#RUN touch /datafolder/Contador.csv

RUN pip install -r requirements.txt


CMD ["python", "main.py"]