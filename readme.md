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
