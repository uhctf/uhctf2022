FROM alpine:latest
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apk add python3
ADD ./src/gen.py /gen.py
ADD ./src/words /words
ADD ./src/server.py /server.py

ENV TRESHOLD 1000000000000
ENV FLAG "uhctf{grandma-really-likes-these-c73266⏎}"
EXPOSE 2000
ENTRYPOINT ["/usr/bin/python3"]
CMD ["/server.py", "2000"]
