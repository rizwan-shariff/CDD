Folder for experiment 8. The container is run directly from the stock `nginx`
image, so no build context is needed:

```bash
docker pull nginx
docker run -d --name nginx-lab -p 8080:80 nginx
```

The default nginx welcome page is served on <http://localhost:8080>.
