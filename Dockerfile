FROM python:3.9.7


RUN apt-get update

WORKDIR /app
COPY python_code/main.py /app
COPY python_code/requirements.txt /app

RUN pip install -r requirements.txt


CMD ["python", "main.py"]