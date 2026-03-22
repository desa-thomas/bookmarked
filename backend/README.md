# Backend

## Project Setup 
- Make sure python3 and PIP are installed 
- `cd bookmarked/backend` 
- create a python virtual enironment - `python3 -m venv {venvDirName}`
- Download project dependencies - `pip install -e .`
- Now the project is setup on your machine
- Start backend server (include instructions once this is setup)

## Project Structure
```
.../backend/ 
|
| - README.md
| - api.py 
| 
| - controllers/ 
    |
    | - __init__.py 
    | - TestController.py 
|
| - entities/ 
    |
    | - __init__.py 
    | - TestEntity.py 
```

Modules from `controller/` and `entities/` are importable from `backend/api.py` using : `import className from controllers.fileName`
