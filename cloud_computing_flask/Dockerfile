FROM ubuntu:18.04

RUN apt-get update && apt-get -y install python3.7 python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 80

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
