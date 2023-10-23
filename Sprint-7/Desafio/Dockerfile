FROM ubuntu:22.04
RUN apt-get update
WORKDIR /app
RUN apt-get install -y tzdata
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3
RUN apt install -y python3-pip
RUN pip3 install boto3
COPY teste.py /app/teste.py
COPY movies.csv /app/movies.csv
COPY series.csv /app/series.csv
