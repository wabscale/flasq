FROM ubuntu:18.04

ENV CERTPATH=default
ENV SITENAME=default
ENV WORKERS=8
ENV PORT=5000

RUN apt update
RUN apt install -y python3 python3-pip

RUN useradd -ms /bin/bash flasq

COPY requirements.txt /home/flasq/site/
WORKDIR /home/flasq/site

RUN mkdir -p /etc/letsencrypt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

RUN mkdir -p ~/site/web/data
RUN chown -R flasq /home/flasq
USER flasq

CMD gunicorn --config gunicorn_config.py web:app
