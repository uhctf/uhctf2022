# Deployment
1. Copy `default.env` to `oracle/.env` and fill in the values
2. `docker build -t <image_name> .`
3. `docker run -p <port>:420 --rm <image_name>`

Note: performance in Docker is subpar.