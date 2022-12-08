# MNIST Digits
## Installation
For compatibility purposes, it is necessary to set up a virtual environment on the project.

### 1. Python Version control
- Use `pyenv` for installing desired python version. Install using `brew install pyenv`. Below are some useful pyenv commands.
```
pyenv versions
pyenv install 3.10.6
pyenv.uninstall <version>
```
- Set up python version in your local project
```
<your_project># pyenv local 3.10.6
```

### 2. Virtual Env Creation & Activation

- `python3 -m venv venv` for initialising the virtual environment
- `source venv/bin/activate` for activating the virtual environment
- An `env` directory shall be created in your project. Take note to include it in `.gitignore`

### 3. Dependency Installation
- `pip install --upgrade pip` for upgrading the pip
- `pip install -r requirements.txt` for the functional dependencies