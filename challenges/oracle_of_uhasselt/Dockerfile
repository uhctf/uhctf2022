FROM rust:slim-buster

# Note: only the contents are copied
COPY ./oracle/ /usr/src/app/
WORKDIR /usr/src/app/

RUN apt-get update && apt-get install -y socat openssl libssl-dev pkg-config
RUN cargo install --path .

EXPOSE 420
CMD socat tcp-l:420,reuseaddr,fork system:'oracle'