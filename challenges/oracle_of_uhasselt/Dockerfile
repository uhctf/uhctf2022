FROM python:3.9.10-slim

# Note: only the contents are copied
COPY ./src/ /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 23
CMD python ./main.py