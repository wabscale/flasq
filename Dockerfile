FROM python:3.7

ENV SITENAME=flasq
ENV WORKERS=8
ENV PORT=5000

RUN useradd -ms /bin/bash flasq

COPY . /home/flasq/${SITENAME}
WORKDIR /home/flasq/${SITENAME}

RUN mkdir -p /etc/letsencrypt
RUN pip3 install -r requirements.txt

RUN mkdir -p ~/${SITENAME}/web/data
RUN chown -R flasq /home/flasq
USER flasq

CMD gunicorn --config gunicorn_config.py web:app
