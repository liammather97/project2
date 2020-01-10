FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /service1/requirements.txt
WORKDIR /service1
RUN pip install -r requirements.txt
COPY . /service1
ENTRYPOINT [ "python", "app.py" ]