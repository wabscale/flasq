FROM ubuntu:18.04
MAINTAINER big_J

ENV NAME=Site
ENV PORT=1337

COPY . /${NAME}
WORKDIR /${NAME}

RUN apt-get update
RUN apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    gunicorn
RUN ./setup.sh
RUN source ./activate

CMD gunicorn -b 0.0.0.0:${PORT} -w 8 app:app 0.0.0.0 ${PORT}
