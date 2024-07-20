FROM python:3.9
RUN apt-get update 
RUN apt-get install -y nginx 

RUN apt-get install -y systemd
RUN apt-get -y install spawn-fcgi
RUN apt-get -y install libgomp1
RUN apt-get update 
RUN apt-get -y install default-mysql-client 


RUN apt-get -y install php-fpm php-mysql
COPY . /VisionXplorer
WORKDIR /VisionXplorer
RUN groupadd -g 1001 cvGroup

RUN useradd -r -m -u 1001 -g cvGroup cvUser
RUN rm -rf /var/lib/apt/lists/*
USER cvUser

RUN pip install -r requirements.txt

ENTRYPOINT "/VisionXplorer/apps/startScript.sh"
