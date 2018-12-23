FROM python:3.7


RUN useradd -ms /bin/bash flasq

COPY . /home/flasq/${SITENAME}
WORKDIR /home/flasq/${SITENAME}

RUN mkdir -p /etc/letsencrypt
RUN pip3 install -r requirements.txt

RUN chown -R flasq /home/flasq
USER flasq
CMD gunicorn --config gunicorn_config.py web:app
