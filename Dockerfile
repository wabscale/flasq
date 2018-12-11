FROM python:3.7

ENV NAME=flasq
ENV PORT=5000
ENV WORKERS=8

COPY . /home/${NAME}
WORKDIR /home/${NAME}

RUN pip3 install -r requirements.txt
CMD gunicorn -b 0.0.0.0:${PORT} -w ${WORKERS} web:app
