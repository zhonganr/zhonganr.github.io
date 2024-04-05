![](src/static/logo.png)

[![](https://img.shields.io/github/actions/workflow/status/ai-atoms/milady-docs/main.yml?branch=main&label=docs%20build&style=for-the-badge)](https://ai-atoms.github.io/milady-docs/)

## Contents

This repository hosts the documentation of the `Milady 2.0` software package.

## Local build instructions

### Setup Python environment

Deactivate any conda or virtual environment that could be activated, and do: 

```bash
python -m venv env 
source env/bin/activate
pip install -r src/requirements.txt
```

### Build and show in browser

```
cd src 
make -B html
python3 -m http.server -d build/html
firefox http://0.0.0.0:8000/
```
