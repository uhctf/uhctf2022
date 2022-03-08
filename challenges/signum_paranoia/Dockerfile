FROM python:alpine3.15

# Note: only the contents are copied
COPY ./src/ /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 wsgi:app