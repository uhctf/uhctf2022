# Deployment

To deploy, build and run the Docker. This might take a while, as both front and backend have to be compiled.

```bash
docker build -t nanflags .
docker run -p 80:80 nanflags
```
