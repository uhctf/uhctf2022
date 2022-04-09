FROM alpine:3.15
WORKDIR /app
COPY . /app
RUN /app/build.sh
CMD ["/app/run.sh"]