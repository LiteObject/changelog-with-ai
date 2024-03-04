# Basic Commands

## Create virtual python environment
    virtualenv -p python3.11 env_name

OR

    python -m venv env_name

## Activate the virtual env
    env_name/scripts/activate

## Update pip
    py -m pip install --upgrade pip

## Check all installed packages
    pip list

## Install Packages
    pip install requests

---
## Create a file listing all required dependencies of the Python project
    pip freeze > requirements.txt

## Install dependencies from requirements.txt:
    pip install -r requirements.txt
