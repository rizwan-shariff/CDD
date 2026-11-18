# Docker laboratory work

Artefacts for experiments 8 to 11 of the CDD laboratory course.

| Folder | Experiment | What it contains |
|---|---|---|
| `exp8-nginx/` | Docker images and containers | notes and the commands used to run the stock `nginx` image |
| `exp9-custom-image/` | Dockerfile and custom image | `Dockerfile` that serves a custom page from `nginx` |
| `exp10-compose/` | Multi-container application | `docker-compose.yml` running the site plus a second `docker` image container |
| `exp11-python-app/` | Containerised Python application | `Dockerfile` that runs `calculator.py` inside `python:3.12-slim` |

All commands below are run from the repository root in Git Bash.

## Experiment 8 - run a simple application with the nginx image

```bash
docker pull nginx
docker run -d --name nginx-lab -p 8080:80 nginx
docker ps
docker images
```

Open <http://localhost:8080> to see the default nginx welcome page.

## Experiment 9 - build a custom image from a Dockerfile

```bash
docker build -t cdd-custom-nginx:1.0 docker/exp9-custom-image
docker run -d --name custom-web -p 8081:80 cdd-custom-nginx:1.0
docker ps
```

## Experiment 10 - run two containers with Docker Compose

```bash
docker compose -f docker/exp10-compose/docker-compose.yml up -d
docker compose -f docker/exp10-compose/docker-compose.yml ps
```

The stack runs `web` (the `nginx` image serving `exp10-compose/site` on port
8082) and `tool` (the `docker` image, published on port 8083), so both images
used in the laboratory run together under one Compose project.

## Experiment 11 - containerise a Python application

```bash
docker build -t cdd-calculator:1.0 docker/exp11-python-app
docker run --rm cdd-calculator:1.0
```

The image copies `calculator.py` into `python:3.12-slim` and runs it, so the four
arithmetic results are printed from inside the container.

## Clean up

```bash
docker rm -f nginx-lab custom-web
docker compose -f docker/exp10-compose/docker-compose.yml down
docker rmi cdd-custom-nginx:1.0 cdd-calculator:1.0
```
