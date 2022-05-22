FROM python:3.10-alpine
WORKDIR /app
ADD requirements.txt /app
ADD src /app/src
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:80", "--chdir", "src", "app:app"]
