FROM python:3.10-alpine

RUN apk update

RUN apk add git

ENV FLASK_APP=main.py

WORKDIR /flaskcrud

COPY ./requirements.txt /flaskcrud

RUN pip install -r requirements.txt

COPY . /flaskcrud

CMD [ "flask", "run", "--host=0.0.0.0", "--debug"]