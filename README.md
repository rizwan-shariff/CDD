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
| 8 | UI/UX prototyping | Figma frames, components and clickable prototype flows | `figma/` |

## Repository layout

```text
CDD/
├── .github/workflows/
│   ├── ci.yml                  # Python CI
│   └── build-test.yml          # Calculator build and unit tests
├── conflict_class/             # merge-conflict exercise
├── devops lab1/ ... lab5/      # experiment artefacts
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

## Figma prototypes

The final experiment moves from code to design. `figma/` contains the exported
boards for two prototypes:

- **YouScream** — four desktop screens with different colour themes, shared
  components and a clickable flow.
- **F1_PAGE** — a fourteen-screen motorsport portal connected as one prototype.

More detail, including the individual design boards, is in
[`figma/README.md`](figma/README.md).

## Notes

- The repository is public so that the Actions runs and commit history can be
  inspected.
- The lab artefacts are intentionally simple; the focus is on understanding the
  workflow rather than building a large application.
