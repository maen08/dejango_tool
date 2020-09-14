#!/usr/bin/python3
import os

# installing the packages required
pip install psycopg2-binary gunicorn django-heroku dj-database-url

# create a requirements.txt file
pip freeze > requirements.txt

# create a Procfile
project_directory = os.getcwd()
split_dirs = project_directory.split('/')
project_name = split_dirs[-1]

# print(project_name)   # code to check if the project_name is correct

with open('Procfile', 'x') as f:
    f.write('web: gunicorn ' +project_name+'.wsgi:application')  # make sure the project name is correct


print('hello am running')
