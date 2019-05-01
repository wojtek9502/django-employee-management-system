### Employee Management System


### Installation

EMS requires:
- Python 3.7+
- "config.ini" file in "employee-management-system/" folder

You should create superuser account. 
Creating a superuser account using the "python manage.py createsuperuser" command requires entering: username, email and password

Install dependencies, migrate, createsuperuser and run server:

```sh
$ cd employee-management-system/
$ pip install -r requirements.txt 
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage,py runserver
```

Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)
