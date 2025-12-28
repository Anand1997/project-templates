# < Project Template > Python
Offline-friendly Python project template.
### Setup (offline)
```shell
# create venv
python -m venv .venv

# Install wheels (if any)
pip install --no-index --find-links=./wheels pytest mypy

# Run main 
python -m my_project.main 
```
### How to use `requirements` folder
On online machine 
```shell
# create requirements file
$ pip install gitpython 
$ pip freeze > requirements/base.txt

# download requirements  
$ pip download -r requirements/base.txt -d wheels/
```
On offline machine 
```shell
$ pip install --no-index --find-links=./wheels -r requirements/base.txt
```