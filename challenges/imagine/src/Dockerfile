FROM wordpress:php8.1

RUN apt-get update && apt-get install -y wget unzip
ENV WORDPRESS_DB_HOST=192.168.0.3:3307

WORKDIR /usr/src/wordpress

COPY ./flag.zip ./theme.zip

RUN wget https://downloads.wordpress.org/theme/shopper-shop.1.0.2.zip -O ./theme.zip
RUN unzip theme.zip
RUN mv shopper-shop ./wp-content/themes/

WORKDIR /var/www/html/