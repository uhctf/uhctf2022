FROM alpine:latest
ENV IP=172.17.0.2
EXPOSE 53/udp 80/tcp

# DNS Setup

RUN apk add nsd
COPY nsd.conf /etc/nsd/nsd.conf
COPY uhctf.dev.zone /etc/nsd/uhctf.dev.zone
RUN sed -i  "s/IPADDR/$IP/g" /etc/nsd/uhctf.dev.zone

# Nginx Setup

RUN apk add nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY home.html /www/home/index.html
COPY 404.html /www/404/index.html
COPY droids.gif /www/404/droids.gif
COPY flag.html /www/flag/index.html

# Run command

RUN apk add supervisor
COPY supervisord.conf /etc/supervisord.conf 

ENTRYPOINT ["supervisord"]
