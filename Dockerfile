FROM python:3.7

ENV NAME=Site
ENV PORT=5000

COPY . /home/${NAME}
WORKDIR /home/${NAME}


RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:${PORT} -w 8 web:app
