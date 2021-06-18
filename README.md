# Веб-приложение для планирования поездок и мероприятий

## Build Setup

```bash
# install virtual environment create tool
$ pip install virtualenv

# create virtual environment
$ virtualenv venv

# activate venv
source venv/bin/activate  # on Linux
venv\Scripts\activate.bat  # on Windows

# install dependencies
(venv) $ pip install -r requirements.txt

# make migrations
(venv) $ python manage.py migrate

# run server
(venv) $ python manage.py runserver

# deactivate venv
(venv) $ deactivate  # on Linux
(venv) $ deactivate.bat  # on Windows 
```
