# try_django

#Virtual Environment

python3 -m venv try_django

#Activate virtual Env

. try_django/bin/activate
source try_django/bin/activate

#Deactivate virtual Env
Deactivate

#Install django with pip3
pip3  install Django==2.2

#startproject 
django-admin startproject try_django . # here . means this folder

#To run development server
./manage.py runserver
python3 manage.py runserver

#Makemigrations and migrate
./manage.py makemigrations
python3 manage.py makemigrations

./manage.py migrate
python3 manage.py migrate

#command to create superuser 
python3 manage.py createsuperuser
Username (leave blank to use 'aps'): Aps
Email address: admin@thesocialtalks.com


./manage.py shell
Python 3.8.5 (default, Jul 20 2020, 00:00:00) 
[GCC 10.1.1 20200507 (Red Hat 10.1.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.conf import settings
>>> settings.BASE_DIR
'/home/Aps/try_django'
>>> import os
>>> os.path.join(BASE_DIR, 'templates')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'BASE_DIR' is not defined
>>> BASE_DIR = settings.BASE_DIR
>>> os.path.join(BASE_DIR, 'templates')
'/home/Aps/try_django/templates'

