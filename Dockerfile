FROM python:3.9-slim
MAINTAINER Ekaterina Lapina
RUN apt-get update -y
COPY . /opt/gsom_predictor 
WORKDIR /opt/gsom_predictor
RUN apt install -y python3-pip
RUN pip install -r requirements.txt
CMD python3 app.py
