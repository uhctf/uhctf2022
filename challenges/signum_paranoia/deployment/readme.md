# Deployment
1. Copy `default.env` to `src/.env` and fill in the values
2. `docker build -t <image_name> .`
3. `docker run -p <port>:80 --rm <image_name>`
