## ref https://github.com/tebeka/pythonwise/blob/master/docker-miniconda/Dockerfile
#FROM ubuntu:18.04
#
## System packages
#RUN apt-get update && apt-get install -y curl
#
## Install miniconda to /miniconda
#RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
#RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
#RUN rm Miniconda3-latest-Linux-x86_64.sh
#ENV PATH=/miniconda/bin:${PATH}
#RUN conda update -y conda
#
## Python packages from conda
#RUN conda install -c anaconda -y python=3.7.2
#
#
## Setup application
##COPY imgsrv.py /
##ENTRYPOINT ["/miniconda/bin/python", "/imgsrv.py"]
##EXPOSE 8080
#RUN pip install --upgrade pip
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["python", "./app.py", "runserver", "0.0.0.0:8000"]
#
#COPY /data/train.csv /app/train.csv
#COPY /data/test.csv /app/test.csv

#쓰앵님 설정 파일 내용
FROM python:3.8-slim-buster AS builder
ADD . .
COPY /data/train.csv /app/train.csv
COPY /data/test.csv /app/test.csv
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","-m","unittest","discover","-s","tests"]