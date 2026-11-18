# CDD Lab Portfolio

**Rizwan Shariff S M** · USN **4NI25CS163**  
**1BCS303 — Collaborative Development and DevOps**  
Department of Computer Science and Engineering, NIE Mysuru

![Python CI](https://github.com/rizwan-shariff/CDD/actions/workflows/ci.yml/badge.svg)
![Calculator Build and Test](https://github.com/rizwan-shariff/CDD/actions/workflows/build-test.yml/badge.svg)

---

## About this repository

This repository is my working record for the CDD laboratory course. It contains
the artefacts produced in each experiment — from the first Git commit through to
a Figma prototype — together with the GitHub Actions workflows that automate the
Python checks.

The experiments are deliberately small. Each folder isolates one idea, so the
repository can be read in order or opened at the experiment that interests you.

## Lab overview

| # | Experiment | What it demonstrates | Key files |
|:-:|---|---|---|
| 1 | Git basics | Repository setup, staging, committing, reading `git log` | `student.txt` |
| 2 | Remote synchronisation | `clone`, `push`, `fetch`, `pull`, remote tracking | `devops lab1/`, `devops lab2/` |
| 3 | Branching and merging | Feature branches, merge conflicts, rebase, history graph | `conflict_class/`, `devops lab3/` |
| 4 | Forks and issues | Fork workflow, issue templates, feature branch source file | `devops lab4/` |
| 5 | Team collaboration | Shared repository, pull request flow, branch hygiene | `devops lab5/`, `login.txt` |
| 6 | CI with GitHub Actions | YAML workflow that runs a Python program on every push | `hello.py`, `ci.yml` |
| 7 | Automated build and test | Calculator module and unittest suite executed by CI | `calculator.py`, `test_calculator.py`, `build-test.yml` |
| 8 | Docker images and containers | Pull `nginx`, run a detached container, publish a port | `docker/exp8-nginx/` |
| 9 | Dockerfiles and custom images | Build a tagged image that serves a custom page | `docker/exp9-custom-image/` |
| 10 | Docker Compose | Two-container stack started with one command | `docker/exp10-compose/` |
| 11 | Containerised Python application | Run `calculator.py` inside `python:3.12-slim` | `docker/exp11-python-app/` |
| 12 | Personas and wireframes | Personas, a user journey and low-fidelity wireframes | `figma/` |
| 13 | High-fidelity prototypes | Figma frames, components and clickable prototype flows | `figma/` |

## Repository layout

```text
CDD/
├── .github/workflows/
│   ├── ci.yml                  # Python CI
│   └── build-test.yml          # Calculator build and unit tests
├── conflict_class/             # merge-conflict exercise
├── devops lab1/ ... lab5/      # experiment artefacts
├── docker/                     # experiments 8-11: nginx, Dockerfile, Compose, Python
├── figma/                      # UI/UX prototypes and design boards
├── calculator.py
├── test_calculator.py
├── hello.py
├── student.txt
├── login.txt
├── login1.txt
├── signup.txt
└── README.md
```

## Continuous integration

Two workflows run on pushes and pull requests to `main`, and both can also be
started manually from the Actions tab.

| Workflow | File | What it does |
|---|---|---|
| Python CI | `.github/workflows/ci.yml` | Checks out the repository, installs Python 3.12 and runs `hello.py` |
| Calculator Build and Test | `.github/workflows/build-test.yml` | Runs `calculator.py`, then `python -m unittest -v test_calculator.py` |

## Run it locally

Python 3.12 is recommended.

```bash
python hello.py
python calculator.py
python -m unittest -v test_calculator.py
```

Expected result: the calculator prints four arithmetic results, and all five
unit tests pass.

## Docker

Experiments 8 to 11 package the work in containers. The `docker/` folder holds
one folder per experiment, and every command is run from the repository root in
Git Bash with the Docker Engine running.

| Experiment | Folder | Image | Host port |
|---|---|---|---|
| 8 - images and containers | `docker/exp8-nginx/` | `nginx:latest` | 8080 |
| 9 - custom image from a Dockerfile | `docker/exp9-custom-image/` | `cdd-custom-nginx:1.0` | 8081 |
| 10 - Compose stack | `docker/exp10-compose/` | `nginx:latest` + `docker:latest` | 8082, 8083 |
| 11 - Python application | `docker/exp11-python-app/` | `cdd-calculator:1.0` | none |

The first experiment pulls the official `nginx` image and runs it as a detached
container named `nginx-lab`. The second adds a `Dockerfile` that copies a custom
page over the default nginx page and builds it as `cdd-custom-nginx:1.0`. The
third describes the web container and a second container from the `docker` image
in one Compose file, so the whole stack starts with a single command. The fourth
copies `calculator.py` into `python:3.12-slim` and runs it, which shows that the
interpreter travels inside the image.

```bash
docker pull nginx
docker run -d --name nginx-lab -p 8080:80 nginx

docker build -t cdd-custom-nginx:1.0 docker/exp9-custom-image
docker run -d --name custom-web -p 8081:80 cdd-custom-nginx:1.0

docker compose -f docker/exp10-compose/docker-compose.yml up -d
docker compose -f docker/exp10-compose/docker-compose.yml ps

docker build -t cdd-calculator:1.0 docker/exp11-python-app
docker run --rm cdd-calculator:1.0
```

More detail, including the Dockerfiles and the full command list, is in
[`docker/README.md`](docker/README.md).

## Figma prototypes

The final experiment moves from code to design. `figma/` contains the exported
boards for two prototypes:

- **Lab website** — a four-screen desktop concept for a shoe brand. Every frame
  keeps the same layout and only the palette changes, and the frames are joined
  as one prototype flow.
- **F1 Student Website** — four team screens (Formula 1, Mercedes, Red Bull,
  McLaren) linked into a single clickable flow.

More detail, including the individual design boards, is in
[`figma/README.md`](figma/README.md).

## Notes

- The repository is public so that the Actions runs and commit history can be
  inspected.
- The lab artefacts are intentionally simple; the focus is on understanding the
  workflow rather than building a large application.
