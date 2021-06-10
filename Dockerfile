FROM python:3.8-slim


WORKDIR /app

#copy project into container
COPY . .

RUN pip3 install -r requirements.txt


