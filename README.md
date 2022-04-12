# Dodgy Bros

## Project Setup
- create a virtual env using command
```bash
    python3.6 -m venv test_env
```

- active virtual env using command
```bash
   source test_env/bin/activate
```
- install requirements using command
```bash
pip3 install -r requirements.txt"
```

- Run migration if db not present
``` bash
python manage.py makemigrations
python manage.py migrate
```
- start server using 
``` bash
python3 manage.py runserver
```

# flake8
- run flake8 to check code quality
``` bash
flake8
```

# Check Code Coverage
```bash
 pytest -n 4 --cov

```

# Black
- For code formating: 
``` bash
black folder/ or filename
```