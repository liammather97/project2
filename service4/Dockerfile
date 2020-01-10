FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /service4/requirements.txt
WORKDIR /service4
RUN pip install -r requirements.txt
COPY . /service4
ENTRYPOINT [ "python", "app.py" ]