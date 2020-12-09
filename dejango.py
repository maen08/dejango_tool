#!/usr/bin/python3
import os
import sys
import subprocess
import logging


# pypi needs this instead of print statements
# change all prints to be logging
# use the colored logging statements


# ask the user to enter the project-name
project_name = input('Whats your project name:')

   
try:
    os.system('pip install gunicorn psycopg2-binary django-heroku dj-database-url')
    print('DONE: All packages are installed successfully')

except FileExistsError:
    print('DONE: All packages are installed successfully')


# create a requirements.txt file
try:
    os.system('pip freeze > requirements.txt')
    print('DONE: requirements.txt file created')

except FileExistsError:
    print('DONE: requirements.txt file created')



# create a Procfile
try:
    with open('Procfile', 'x') as f:
        # make sure the project name is correct
        f.write('web: gunicorn ' + project_name+'.wsgi:application')

except FileExistsError:
    print('DONE: Procfile created')


# project_directory = os.getcwd()
# split_dirs = project_directory.split('/')
# project_folder = split_dirs[-1] 



# a function to prepend the import statement
to_settings = os.chdir(project_name)

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

try:
    line_prepender('settings.py', 'import dj_database_url')
    line_prepender('settings.py', 'import django_heroku')

except FileExistsError:
    print('DONE: All packages are imported')






# print('hello am running')
