FROM node:17-alpine

ADD ./src/ /work/
WORKDIR /work

RUN npm install

CMD set -o allexport; source .env; npm start