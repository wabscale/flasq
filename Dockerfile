FROM python:3.7

ENV NAME="flaskd"
ENV PORT=5000
ENV WORKERS=8

COPY . /${NAME}
WORKDIR /${NAME}

EXPOSE ${PORT}

RUN pip3 install -r requirements.txt
CMD gunicorn -b 0.0.0.0:${PORT} -w ${WORKERS} app:app
