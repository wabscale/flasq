FROM python:3.7-alpine

ENV WORKERS=4
ENV PORT=80

WORKDIR /flasq
COPY requirements.txt .
RUN pip3 install -r requirements.txt \
  && rm requirements.txt

CMD gunicorn --config gunicorn_config.py web:app
