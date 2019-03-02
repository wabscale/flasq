FROM jmc1283/flasq-base

COPY ./requirements.txt /flasq/
RUN pip install -r /flasq/requirements.txt
RUN mkdir -p /flasq/web/.data/

COPY . /flasq
