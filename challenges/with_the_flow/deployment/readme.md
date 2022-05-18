# Deployment
1. Edit flag in `Dockerfile`
2. `docker build -t <image_name> .`
3. Disable ASLR on the Docker host (can't be done in the container)
    - `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`
4. `docker run -p <port>:1337 -v $(pwd)/attachments/:/attachments/ --rm <image_name>`
    - This also compiles the binary for deployment. See `attachments`.
