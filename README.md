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
