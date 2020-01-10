FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /service3/requirements.txt
WORKDIR /service3
RUN pip install -r requirements.txt
COPY . /service3
ENTRYPOINT [ "python", "app.py" ]