#! usr/bin/python3
import os
# installing the packages required
pip install psycopg2-binary gunicorn django-heroku dj-database-url

# create a requirements.txt file
pip freeze > requirements.txt

# create a Procfile
project_directory = os.getcwd()
directory_list = project_directory.split()
project_name = directory_list[-1]

with open(project_directory) as f:
    f.write('web: gunicorn nameofyourproject.wsgi:application')  # get the name of the project

print('hello am running')