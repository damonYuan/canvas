Canvas
====

# How to install and run

Best practice is to create a virtualenv in the first place,
```
python3 -m venv ./venv
```
Then

```
source venv/bin/activate
pip install -e .
canvas
```

# How to run from source code

## run as module

`python -m canvas.app`

## run as script

`python canvas/app.py`

# How to run the tests

```
source venv/bin/activate
pip install -r requirements.txt
pytest
```

# Assumptions

1. the command input is valid