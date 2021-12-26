# Tibber

# Installation

Create a virtualenv

```bash
virtualenv -p python3 ~/.venv/tibber
```

activate env

```bash
source ~/.venv/tibber/bin/activate
```

and install requirements:

```
pip install -r requirements.txt
```

creata a file called `database.ini` and fill in the db credentials:

```ini
[postgresql]
host=
database=
user=
password=
```

# Populate tables:

Run

```bash
python initialize.py
```
