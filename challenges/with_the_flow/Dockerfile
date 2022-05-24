FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat gcc gcc-multilib

# Note: only the contents are copied
COPY ./src/ /
WORKDIR /

RUN gcc -O3 -fno-stack-protector -m32 /main.c -o /flow

# Add flag
RUN sed 's/puts.*/puts("uhctf{neither-half-empty-nor-half-full-82f1db}");/g' -i /main.c
RUN gcc -O3 -fno-stack-protector -m32 /main.c -o /flow_with_flag

RUN mkdir -p /attachments/
CMD cp /flow /attachments/flow && socat tcp-l:1337,reuseaddr,fork system:'/flow_with_flag'