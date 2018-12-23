FROM python:3.7

ENV SITENAME=default
ENV PORT=443
ENV WORKERS=8

COPY . /home/${SITENAME}
WORKDIR /home/${SITENAME}

RUN mkdir -p ADD /etc/letsencrypt/live/default

RUN pip3 install -r requirements.txt
CMD gunicorn --config guncorn_config.py web:app
