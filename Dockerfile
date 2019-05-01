######################################################
FROM node:12-alpine AS js-build

ENV NODE_ENV="production"

WORKDIR /opt/build
COPY package*.json .

COPY . .

RUN npm install \
  && npm run build \
  && rm -rf \
  node_modules \
  package.json \
  package-lock.json \
  webpack.config.js \
  requirements.txt

######################################################
FROM jmc1283/flasq-base:latest AS flasq

ENV PORT=80
ENV WORKERS=4
WORKDIR /flasq

COPY requirements.txt .

RUN pip3 install -r requirements.txt \
  && mkdir -p /files \
  && rm requirements.txt

COPY --from=js-build /opt/build .
