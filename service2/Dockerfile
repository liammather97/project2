FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /service2/requirements.txt
WORKDIR /service2
RUN pip install -r requirements.txt
COPY . /service2
ENTRYPOINT [ "python", "app.py" ]